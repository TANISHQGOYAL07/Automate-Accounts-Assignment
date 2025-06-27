import os
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from .db import SessionLocal, engine
from . import models, ocr_utils

models.Base.metadata.create_all(bind=engine)
app = FastAPI()
UPLOAD_DIR = "sample_receipts"

os.makedirs(UPLOAD_DIR, exist_ok=True)
@app.get("/")
def root():
    return {"message": "Welcome to the Receipt OCR API"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        return {"error": "Only PDF files are allowed"}

    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    db = SessionLocal()
    receipt_file = models.ReceiptFile(
        file_name=file.filename,
        file_path=file_path,
        is_valid=False,
        is_processed=False
    )
    db.add(receipt_file)
    db.commit()
    db.refresh(receipt_file)
    db.close()

    return {"message": "File uploaded", "id": receipt_file.id}

@app.post("/validate")
def validate_file(id: int):
    db = SessionLocal()
    receipt_file = db.query(models.ReceiptFile).filter_by(id=id).first()
    if not receipt_file:
        return {"error": "Receipt not found"}

    try:
        import fitz  # PyMuPDF
        with fitz.open(receipt_file.file_path) as pdf:
            pdf.page_count
        receipt_file.is_valid = True
        receipt_file.invalid_reason = None
    except Exception as e:
        receipt_file.is_valid = False
        receipt_file.invalid_reason = str(e)

    db.commit()
    db.refresh(receipt_file)
    db.close()
    return {"is_valid": receipt_file.is_valid, "reason": receipt_file.invalid_reason}

@app.post("/process")
def process_file(id: int):
    db = SessionLocal()
    receipt_file = db.query(models.ReceiptFile).filter_by(id=id).first()
    if not receipt_file or not receipt_file.is_valid:
        return {"error": "Receipt not found or invalid"}

    text = ocr_utils.extract_text_from_pdf(receipt_file.file_path)
    data = ocr_utils.extract_receipt_info(text)

    receipt = models.Receipt(
        merchant_name=data["merchant_name"],
        purchased_at=data["purchased_at"],
        total_amount=data["total_amount"],
        file_path=receipt_file.file_path
    )
    db.add(receipt)
    receipt_file.is_processed = True
    db.commit()
    db.refresh(receipt)
    db.close()
    return {"message": "Receipt processed", "receipt": data}

@app.get("/receipts")
def get_receipts():
    db = SessionLocal()
    receipts = db.query(models.Receipt).all()
    db.close()
    return receipts

@app.get("/receipts/{id}")
def get_receipt(id: int):
    db = SessionLocal()
    receipt = db.query(models.Receipt).filter_by(id=id).first()
    db.close()
    if not receipt:
        return JSONResponse(content={"error": "Receipt not found"}, status_code=404)
    return receipt

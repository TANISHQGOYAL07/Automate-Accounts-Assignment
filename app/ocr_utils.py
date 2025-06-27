import pytesseract
from pdf2image import convert_from_path
import re
import os

def extract_text_from_pdf(pdf_path):
    images = convert_from_path(pdf_path)
    text = ''
    for img in images:
        text += pytesseract.image_to_string(img)
    return text

def extract_receipt_info(text):
    merchant = text.split("\n")[0]
    date_match = re.search(r"\d{2}/\d{2}/\d{4}", text)
    amount_match = re.search(r"(Total|Amount)[^\d]*(\d+[\.,]?\d+)", text, re.IGNORECASE)
    
    return {
        "merchant_name": merchant.strip(),
        "purchased_at": date_match.group() if date_match else None,
        "total_amount": float(amount_match.group(2)) if amount_match else None
    }

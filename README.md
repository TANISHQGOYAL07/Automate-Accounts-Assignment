## 🛠️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/automate-accounts-developer-hiring-assessment.git
cd automate-accounts-developer-hiring-assessment
2. Create and Activate Virtual Environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Make Sure Tesseract OCR is Installed
bash
Copy
Edit
# For macOS
brew install tesseract

# For Ubuntu/Debian
sudo apt install tesseract-ocr
🚀 Run the Project
Start the FastAPI server using Uvicorn:

bash
Copy
Edit
uvicorn app.main:app --reload
Then open:

API Root: http://127.0.0.1:8000

API Docs (Swagger UI): http://127.0.0.1:8000/docs

🔌 API Endpoints (with Example Usage)
📨 POST /upload
Upload a PDF receipt.

Example (via Swagger or cURL):

bash
Copy
Edit
curl -F "file=@sample_receipts/sample1.pdf" http://127.0.0.1:8000/upload
✅ POST /validate
Validate whether the uploaded file is a valid PDF.

Request Body:

json
Copy
Edit
{
  "file_id": 1
}
🧠 POST /process
Run OCR and extract receipt data.

Request Body:

json
Copy
Edit
{
  "file_id": 1
}
📃 GET /receipts
Get all extracted receipts from the database.

🔍 GET /receipts/{id}
Get details of a single receipt by ID.

💾 Database
All data is stored in:

bash
Copy
Edit
receipts.db

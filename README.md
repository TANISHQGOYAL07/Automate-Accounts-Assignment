

## 🛠️ Setup & Installation🚀

**1)Clone the Repository**

git clone https://github.com/TANISHQGOYAL07/Automate-Accounts-Assignment.git
cd Automate-Accounts-Assignment

**2)Create and Activate Virtual Environment**

python3 -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate   # For Windows


**3)Install Python Dependencies**

pip install -r requirements.txt

**4)Install Tesseract OCR**

For macOS
brew install tesseract

For Ubuntu/Linux
sudo apt install tesseract-ocr

**
5) How to Run the Project**
Start the development server using:


uvicorn app.main:app --reload
Once running, open your browser and go to:

Swagger UI: http://127.0.0.1:8000/docs

API root: http://127.0.0.1:8000

**6) API Endpoints**
POST /upload
Upload a receipt (PDF file only).

i) POST /validate
Validate whether a file is a proper PDF.

Request Body Example:
{ "file_id": 1 }

ii) POST /process
Run OCR on the receipt and extract key data.

Request Body Example:

{ "file_id": 1 }

iii) GET /receipts
List all processed receipts in the database.

iv) GET /receipts/{id}
Fetch a specific receipt by its unique ID.


**💾 Database Details**
All extracted data is saved in a local SQLite database file called receipts.db. You can view or inspect it using tools like DB Browser for SQLite.

**🧪 Sample Receipts**
You can test the OCR by placing scanned PDF receipts inside the year-based folders provided (e.g., 2018/, 2019/, etc.).

**👤 Author**
Tanishq Goyal
🔗 GitHub -https://github.com/TANISHQGOYAL07
🔗 LinkedIn - https://www.linkedin.com/in/tanishq-goyal-162975275/



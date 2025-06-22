conda create -n venv python=3.10 -y

conda activate venv

pip install -e .

pip list

# 📇 BizCardX: Extracting Business Card Data with OCR

A Streamlit web app that extracts information from uploaded business card images using **EasyOCR** and stores the data in a **PostgreSQL database**. It also supports viewing, editing, and deleting stored records.

---

## 🚀 Features

- OCR extraction using `easyOCR`
- Regex parsing of:  
  ✔️ Name, ✔️ Designation, ✔️ Email, ✔️ Phone, ✔️ Website  
  ✔️ Company, ✔️ City, ✔️ State, ✔️ Pincode
- Stores data in PostgreSQL (with user-authentication)
- View/Edit/Delete operations with Streamlit GUI
- Image display from DB using `BytesIO`
- MongoDB integration to fetch sample raw data
- Sidebar-based navigation using `streamlit_option_menu`

---

## 🛠️ Tech Stack

| Tool            | Purpose                         |
|----------------|----------------------------------|
| Python          | Core language                   |
| Streamlit       | Frontend Web App                |
| EasyOCR         | Optical Character Recognition   |
| PostgreSQL      | Primary data storage            |
| pymongo         | Fetching example data           |
| psycopg2        | PostgreSQL integration          |
| Pillow, Regex   | Image handling & pattern matching|

---

## 🧩 Folder Structure

BizCardX_OCR/
│
├── app/
│ ├── data_extraction.py
│ ├── database.py
│ ├── image_utils.py
│
├── config/
│ └── init.py
├── exception/
│ └── exceptions.py
│
├── streamlit_ui.py # 🚀 Main UI file
├── unit_test.py # ✅ Tests for OCR and DB
├── setup.py
├── main.py # Optional logic wrapper
├── requirements.txt
└── README.md
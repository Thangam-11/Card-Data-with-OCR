from app.data_extraction import BizCardExtractor
from app.db_handler import MongoDBHandler

extractor = BizCardExtractor(debug=True)
db = MongoDBHandler()

# Replace with actual image path
image_path = "data_src\1.png"
extracted_data = extractor.extract_all(image_path)
db.insert_data(extracted_data)

print("Data extracted and inserted successfully.")
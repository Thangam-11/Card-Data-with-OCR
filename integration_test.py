import os
from app.data_extraction import BizCardExtractor
from app.db_handler import MongoDBHandler
from exception.exceptions import OcrdataException

if __name__ == "__main__":
    # Initialize classes
    extractor = BizCardExtractor(debug=True)
    db = MongoDBHandler()

    # Step 1: Use an existing image (ensure this file exists)
    image_path = os.path.join("data_src", "1.png")  # Change path if needed

    try:
        # Step 2: Extract data using EasyOCR
        extracted_data = extractor.extract_all(image_path)
        print("\n🔍 Extracted Data:")
        for k, v in extracted_data.items():
            print(f"{k}: {v}")

        # Step 3: Insert extracted data into MongoDB
        inserted_id = db.insert_data(extracted_data)
        print(f"\n✅ Inserted into MongoDB with ID: {inserted_id}")

        # Step 4: Read all data
        all_data = db.get_all_data()
        print("\n📄 Data in MongoDB:")
        for record in all_data:
            print(record)

        # Step 5: Update test (just for demo, updating company name)
        updated = db.update_data({"email_address": extracted_data["email_address"]},
                                 {"company_name": "Updated Company"})
        print(f"\n🛠 Updated count: {updated.modified_count}")

        # Step 6: Delete test
        deleted = db.delete_data({"email_address": extracted_data["email_address"]})
        print(f"\n❌ Deleted count: {deleted.deleted_count}")

    except FileNotFoundError:
        print("❌ Error: Image file not found. Check the image path.")
    except OcrdataException as e:
        print(str(e))
    except Exception as ex:
        print(f"⚠️ Unexpected Error: {ex}")

from app.db_handler import MongoDBHandler
import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    db = MongoDBHandler()

    # Sample data
    test_data = {
        "card_holder_name": "Alice Smith",
        "email_address": "alice@example.com",
        "company_name": "AliceTech",
        "mobile_number": "9876543210"
    }

    # 🟢 Insert Test
    inserted_id = db.insert_data(test_data)
    print(f"\n✅ Inserted ID: {inserted_id}")

    # 🔵 Read Test
    data = db.get_all_data()
    print("\n🔍 All Records:")
    for d in data:
        print(d)

    # 🟡 Update Test
    updated = db.update_data({"email_address": "alice@example.com"}, {"company_name": "UpdatedTech"})
    print(f"\n🛠 Updated Count: {updated.modified_count}")

    # 🔴 Delete Test
    deleted = db.delete_data({"email_address": "alice@example.com"})
    print(f"\n❌ Deleted Count: {deleted.deleted_count}")

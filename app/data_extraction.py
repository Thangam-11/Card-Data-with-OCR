# === data_extraction.py ===
import easyocr
import re
from typing import List, Dict
from exception.exceptions import OcrdataException

class BizCardExtractor:
    def __init__(self, debug: bool = False):
        self.reader = easyocr.Reader(['en'], gpu=False)
        self.debug = debug

    def extract_text(self, image_path: str) -> List[str]:
        try:
            results = self.reader.readtext(image_path, detail=0)
            if self.debug:
                print(f"[DEBUG] Raw OCR Text: {results}")
            return results
        except Exception as e:
            raise OcrdataException(f"Error in OCR extraction: {str(e)}", e)

    def clean_text(self, raw_data: List[str]) -> List[str]:
        cleaned = []
        for line in raw_data:
            for part in re.split(r'[;,]', line):
                if part.strip():
                    cleaned.append(part.strip())
        if self.debug:
            print(f"[DEBUG] Cleaned OCR Lines: {cleaned}")
        return cleaned

    def extract_fields(self, lines: List[str]) -> Dict[str, str]:
        info = {
            "company_name": "",
            "card_holder_name": "",
            "designation": "",
            "mobile_number": "",
            "email_address": "",
            "website_url": "",
            "area": "",
            "city": "",
            "state": "",
            "pincode": ""
        }

        phone_pattern = r"[+]?\d{1,4}[-\s]?\d{2,5}[-\s]?\d{4,6}"
        email_pattern = r"[a-zA-Z0-9.\-+_]+@[a-zA-Z0-9.\-+_]+\.[a-z]+"
        web_pattern = r"(www\.[a-zA-Z0-9\-\.]+\.[a-z]+)"

        phones = []
        for line in lines:
            if re.search(email_pattern, line):
                info["email_address"] = re.search(email_pattern, line).group()
            elif re.search(phone_pattern, line):
                phones.append(re.search(phone_pattern, line).group())
            elif re.search(web_pattern, line):
                info["website_url"] = re.search(web_pattern, line).group()

        info["mobile_number"] = " / ".join(phones)

        if lines:
            info["card_holder_name"] = lines[0]
            info["designation"] = lines[1] if len(lines) > 1 else ""
            info["company_name"] = lines[-1]

        return info

    def extract_all(self, image_path: str) -> Dict[str, str]:
        raw_text = self.extract_text(image_path)
        cleaned = self.clean_text(raw_text)
        extracted_fields = self.extract_fields(cleaned)

        if self.debug:
            print(f"[DEBUG] Extracted Info: {extracted_fields}")
        return extracted_fields


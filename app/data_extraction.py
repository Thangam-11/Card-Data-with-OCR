import easyocr
import re
from typing import List, Dict
from exception.exceptions import OcrdataException
from PIL import Image
import numpy as np


class BizCardExtractor:
    def __init__(self):
        self.reader = easyocr.Reader(['en'], gpu=False)

    def extract_text(self, image_path):
        results = self.reader.readtext(image_path, detail=0)
        return results

    def clean_text(self, raw_data):
        data = []
        for line in raw_data:
            for part in re.split(r'[;,]', line):
                if part.strip():
                    data.append(part.strip())
        return data

    def extract_fields(self, lines):
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

        # Simple regex-based field extraction
        phone_pattern = r"[+]?\d{2,4}[-\s]?\d{3,5}[-\s]?\d{4,6}"
        email_pattern = r"[a-zA-Z0-9\.\-+_]+@[a-zA-Z0-9\.\-+_]+\.[a-z]+"
        web_pattern = r"(www\.[a-zA-Z0-9\-\.]+\.[a-z]+)"

        for line in lines:
            if re.search(email_pattern, line):
                info["email_address"] = line
            elif re.search(phone_pattern, line):
                info["mobile_number"] += (line + " / ")
            elif re.search(web_pattern, line):
                info["website_url"] = line

        # Assign placeholders for demo; improve with better NLP/logic
        if lines:
            info["card_holder_name"] = lines[0]
            info["designation"] = lines[1] if len(lines) > 1 else ""
            info["company_name"] = lines[-1]

        return info

    def extract_all(self, image_path):
        raw_text = self.extract_text(image_path)
        cleaned = self.clean_text(raw_text)
        fields = self.extract_fields(cleaned)
        return fields

from app.data_extraction import BizCardExtractor

if __name__ == "__main__":
    extractor = BizCardExtractor()
    # Use a raw string to avoid escape character issues in Windows paths
    data = extractor.extract_all("data_src/1.png")
    print("\n🔍 Extracted Business Card Info:\n")
    for key, value in data.items():
        print(f"{key}: {value}")
    print("\n✅ Extraction completed successfully!")
    print("\n📄 Raw Text Extracted:\n")
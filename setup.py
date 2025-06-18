from setuptools import setup, find_packages

setup(
    name="bizcardx",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Streamlit app to extract and manage business card data using OCR.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/bizcardx",  # Update this with your actual repo URL
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "easyocr==1.7.0",
        "Pillow==10.0.0",
        "numpy==1.25.2",
        "pandas==2.1.0",
        "streamlit==1.26.0",
        "streamlit_option_menu==0.3.6",
        # Uncomment if you're using MongoDB or PostgreSQL
        # "pymongo==4.5.0",
        "psycopg2==2.9.7",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Framework :: Streamlit",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)

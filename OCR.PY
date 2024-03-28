import fitz
import pytesseract
from PIL import Image

def extract_text_with_ocr(pdf_path):
    text = ''
    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        print(f"Error: {e}")
        return None

def save_text_to_file(text, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)

def pdf_to_selectable_text(pdf_path, output_file):
    extracted_text = extract_text_with_ocr(pdf_path)
    if extracted_text:
        save_text_to_file(extracted_text, output_file)
        print(f"PDF converted to selectable text and saved as {output_file}")
    else:
        print("Failed to extract text from the PDF.")

pdf_path = "sample.pdf"
output_file = "output.txt"

pdf_to_selectable_text(pdf_path, output_file)
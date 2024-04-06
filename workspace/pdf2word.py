from PIL import Image
import fitz  # PyMuPDF
import pytesseract
from docx import Document
import string

def sanitize_text(text):
    # Remove non-printable characters and control characters
    printable_chars = set(string.printable)
    sanitized_text = ''.join(filter(lambda x: x in printable_chars, text))
    return sanitized_text

def pdf_to_word_with_ocr(pdf_file, word_file):
    # Open the PDF file
    pdf_document = fitz.open(pdf_file)

    # Create a new Word document
    doc = Document()

    # Extract text using OCR and append to a list
    ocr_text = []
    for page_number in range(len(pdf_document)):
        page = pdf_document.load_page(page_number)
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        text = pytesseract.image_to_string(img)
        sanitized_text = sanitize_text(text)  # Sanitize the extracted text
        ocr_text.append(sanitized_text)

    # Loop through OCR text and insert into the Word document
    for text in ocr_text:
        doc.add_paragraph(text)

    # Save the Word document
    doc.save(word_file)
    print(f"PDF converted with OCR, and saved as '{word_file}'")

# Example usage
pdf_file = 'sample.pdf'
word_file = 'output.docx'
pdf_to_word_with_ocr(pdf_file, word_file)
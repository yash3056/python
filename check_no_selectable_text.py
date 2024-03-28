import fitz

def calculate_non_selectable_text_percentage(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        total_pages = doc.page_count
        pages_without_text = 0
        
        for page in doc:
            text = page.get_text()
            if not text.strip():  # If the page has no non-whitespace text, it's not selectable
                pages_without_text += 1
        
        return (pages_without_text / total_pages) * 100
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    pdf_path = input("Enter the path to the PDF file: ")
    non_selectable_text_percentage = calculate_non_selectable_text_percentage(pdf_path)
    if non_selectable_text_percentage is not None:
        print(f"The percentage of pages without selectable text is: {non_selectable_text_percentage:.2f}%")
    else:
        print("Failed to calculate the percentage.")
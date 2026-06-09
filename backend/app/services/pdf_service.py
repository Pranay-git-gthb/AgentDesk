from pypdf import PdfReader


def extract_pdf_info(pdf_path):

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text

    return {
        "pages": len(reader.pages),
        "text": text
    }
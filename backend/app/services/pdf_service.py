from pypdf import PdfReader


def extract_pdf_info(pdf_path):

    reader = PdfReader(pdf_path)

    texts = []

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            texts.append(page_text)

    text = "".join(texts)
    return {
        "pages": len(reader.pages),
        "text": text
    }

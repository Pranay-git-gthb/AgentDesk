from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path
import shutil

from app.services.pdf_service import extract_pdf_info

router = APIRouter()


@router.post("/upload-pdf")
def upload_pdf(file: UploadFile = File(...)):

    upload_dir = Path("uploads")
    upload_dir.mkdir(parents=True, exist_ok=True)

    filename = Path(file.filename).name
    if not filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported",
        )

    file_path = upload_dir / filename

    try:
        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    finally:
        file.file.close()

    pdf_info = extract_pdf_info(str(file_path))

    return {
        "filename": filename,
        "pages": pdf_info["pages"],
        "characters": len(pdf_info["text"]),
    }

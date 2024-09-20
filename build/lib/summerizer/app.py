from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import os
import tempfile
from summerizer.summarizer import summarize_json, summarize_resume, extract_text_with_uniparse

app = FastAPI()

class JSONData(BaseModel):
    data: dict

class ResumeData(BaseModel):
    text: str

@app.post("/summarize-json/")
async def summarize_json_endpoint(item: JSONData):
    summary = summarize_json(item.data)
    return {"summary": summary}

@app.post("/summarize-resume/")
async def summarize_resume_endpoint(item: ResumeData):
    summary = summarize_resume(item.text)
    return {"summary": summary}


@app.post("/summarize-file/")
async def summarize_file(file: UploadFile = File(...)):
    # Create a temporary file and write the uploaded content to it
    with tempfile.NamedTemporaryFile(delete=False, suffix='.docx') as temp_file:
        temp_file.write(await file.read())
        temp_file_path = temp_file.name

    try:
        # Ensure the file has a valid extension
        if not temp_file_path.endswith(('.pdf', '.docx')):
            raise ValueError(f"Unsupported file type: {temp_file_path}")

        # Extract text from the file using UniParse
        text = extract_text_with_uniparse(temp_file_path)

        # Summarize the extracted text
        summary = summarize_resume(text)
        
        return {"summary": summary}
    finally:
        # Clean up the temporary file
        os.remove(temp_file_path)

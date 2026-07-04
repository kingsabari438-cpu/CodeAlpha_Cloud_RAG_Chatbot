from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from utils.pdf_reader import extract_text_from_pdf
from utils.chunker import split_text_into_chunks
from utils.rag import generate_answer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

uploaded_chunks = []


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "CloudRAG Study Assistant Backend is running 🚀"
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "project": "CloudRAG Study Assistant"
    }


@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    global uploaded_chunks

    if not file.filename.lower().endswith(".pdf"):
        return {
            "success": False,
            "message": "Please upload only PDF file"
        }

    file_bytes = await file.read()
    extracted_text = extract_text_from_pdf(file_bytes)

    if not extracted_text:
        return {
            "success": False,
            "message": "Text not found in PDF"
        }

    chunks = split_text_into_chunks(extracted_text)
    uploaded_chunks = chunks

    return {
        "success": True,
        "filename": file.filename,
        "characters": len(extracted_text),
        "chunks_count": len(chunks),
        "preview": extracted_text[:1000],
        "first_chunk": chunks[0] if chunks else ""
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):
    if not uploaded_chunks:
        return {
            "success": False,
            "answer": "Please upload a PDF first."
        }

    answer = generate_answer(request.question, uploaded_chunks)

    return {
        "success": True,
        "question": request.question,
        "answer": answer
    }
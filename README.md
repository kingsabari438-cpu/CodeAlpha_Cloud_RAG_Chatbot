# CloudRAG Study Assistant

CloudRAG Study Assistant is an AI-powered document question-answering web application.  
It allows users to upload a PDF document and ask questions based on the uploaded content.  
The system extracts text from the PDF, splits it into chunks, retrieves relevant context, and generates answers using Gemini AI.

## Live Demo

Frontend: https://cloudrag-study-assistant.vercel.app/ 
Backend: https://cloudrag-backend-kp9s.onrender.com

## Project Overview

This project is built using AI + Cloud + RAG concept.

RAG stands for Retrieval-Augmented Generation.  
Instead of directly asking the AI model, the system first retrieves relevant information from the uploaded PDF and then sends that context to the AI model to generate a more accurate answer.

## Features

- Upload PDF documents
- Extract text from PDF
- Split extracted text into smaller chunks
- Ask questions from uploaded PDF
- Generate AI-based answers using Gemini API
- FastAPI backend
- Frontend hosted on Vercel
- Backend deployed on Render
- Beginner-friendly AI + Cloud project

## Tech Stack

### Frontend
- HTML
- CSS
- JavaScript
- Vercel

### Backend
- Python
- FastAPI
- Uvicorn
- PyPDF
- Gemini API
- Render

### AI Concept
- RAG
- Text extraction
- Chunking
- Context-based question answering

## Project Structure

```text
cloudrag-study-assistant/
├── backend/
│   ├── utils/
│   │   ├── chunker.py
│   │   ├── pdf_reader.py
│   │   └── rag.py
│   ├── main.py
│   ├── requirements.txt
│   └── .env
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── .gitignore
└── README.md
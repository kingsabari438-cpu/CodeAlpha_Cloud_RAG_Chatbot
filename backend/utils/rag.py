import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def get_relevant_chunks(question: str, chunks: list, top_k: int = 3):
    question_words = question.lower().split()
    scored_chunks = []

    for chunk in chunks:
        chunk_lower = chunk.lower()
        score = 0

        for word in question_words:
            if word in chunk_lower:
                score += 1

        scored_chunks.append((score, chunk))

    scored_chunks.sort(reverse=True, key=lambda x: x[0])

    relevant_chunks = [chunk for score, chunk in scored_chunks[:top_k] if score > 0]

    if not relevant_chunks:
        relevant_chunks = chunks[:top_k]

    return relevant_chunks


def generate_answer(question: str, chunks: list):
    relevant_chunks = get_relevant_chunks(question, chunks)

    context = "\n\n".join(relevant_chunks)

    prompt = f"""
You are CloudRAG Study Assistant.
Answer the user's question only using the given document context.
If the answer is not available in the context, say: "I could not find this in the uploaded PDF."

Document Context:
{context}

User Question:
{question}

Answer in simple student-friendly English.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text
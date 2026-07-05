// Render backend URL inga paste pannu
// Example: const BACKEND_URL = "https://cloudrag-backend.onrender.com";
const BACKEND_URL = " https://cloudrag-backend-kp9s.onrender.com";

async function checkBackend() {
    const statusText = document.getElementById("status");

    try {
        const response = await fetch(`${BACKEND_URL}/health`);
        const data = await response.json();

        statusText.innerText = "Backend connected ✅ " + data.project;
        statusText.style.color = "#22c55e";
    } catch (error) {
        statusText.innerText = "Backend not connected ❌";
        statusText.style.color = "red";
        console.log(error);
    }
}

async function uploadPDF() {
    const fileInput = document.getElementById("pdfFile");
    const previewBox = document.getElementById("pdfPreview");

    if (fileInput.files.length === 0) {
        previewBox.innerText = "Please select a PDF file first.";
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    previewBox.innerText = "Uploading and reading PDF...";

    try {
        const response = await fetch(`${BACKEND_URL}/upload-pdf`, {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        if (data.success) {
            previewBox.innerText =
                "File: " + data.filename + "\n" +
                "Characters: " + data.characters + "\n" +
                "Chunks Created: " + data.chunks_count + "\n\n" +
                "Preview:\n" + data.preview + "\n\n" +
                "First Chunk:\n" + data.first_chunk;
        } else {
            previewBox.innerText = data.message;
        }
    } catch (error) {
        previewBox.innerText = "PDF upload failed.";
        console.log(error);
    }
}

async function askAI() {
    const questionInput = document.getElementById("questionInput");
    const answerBox = document.getElementById("aiAnswer");

    const question = questionInput.value.trim();

    if (question === "") {
        answerBox.innerText = "Please enter a question first.";
        return;
    }

    answerBox.innerText = "AI is thinking...";

    try {
        const response = await fetch(`${BACKEND_URL}/ask`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                question: question
            })
        });

        const data = await response.json();

        if (data.success) {
            answerBox.innerText = data.answer;
        } else {
            answerBox.innerText = data.answer;
        }
    } catch (error) {
        answerBox.innerText = "AI answer failed.";
        console.log(error);
    }
}

checkBackend();
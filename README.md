## AI_Multi_Assistent_Bot
 
Multi-Source AI Chatbot (Flask + Groq LLM + Custom Embeddings).A full-stack AI-powered chatbot that answers questions from PDFs, YouTube videos, websites, and raw text inputs** — built with Python, Flask, and blazing-fast Groq LLM.

## Key Features

- 📄 **PDF Upload & Q&A**: Extracts text, generates embeddings, and allows intelligent querying
- 📺 **YouTube Video Bot**: Transcribes video content using Whisper and supports Q&A
- 🌐 **Website Scraper**: Extracts clean website content for question answering
- ✍️ **Raw Text Upload**: Directly input text for embedding and querying
- ⚡ **Groq LLM API**: Ultra-low latency responses via Groq’s OpenAI-compatible API
- 🔍 **Semantic Search**: Powered by SentenceTransformer + FAISS

---

## 🧱 Tech Stack

| Component        | Technology               |
|------------------|---------------------------|
| Backend          | Python, Flask             |
| Frontend         | HTML (Flask templates)    |
| AI Model         | Groq LLM (OpenAI-compatible) |
| Embeddings       | SentenceTransformer       |
| Vector DB        | FAISS                     |
| Transcription    | OpenAI Whisper            |
| Website Scraping | Requests + BeautifulSoup  |
| Environment      | `.env`, `flask_cors` for CORS handling |

---

## 📂 Project Structure

AI_MULTI_ASSISTANT_BOT/

├── Backend/

│ ├── bots/

│ │ ├── pdf_bot.py

│ │ ├── text_bot.py

│ │ ├── website_bot.py

│ │ └── youtube_bot.py

│ ├── embeddings/

│ │ ├── pdf.py

│ │ ├── text.py

│ │ ├── website.py

│ │ └── youtube.py

│ ├── utils/

│ │ ├── embeddings.py

│ │ ├── pdf.py

│ │ ├── shared_pdf_utils.py

│ │ ├── text.py

│ │ ├── transcriber.py

│ │ └── website.py

│ ├── templates/

│ │ └── index.html

│ └── app.py # Main Flask app entry point
│
├── requirements.txt

└── vercel_wsai.py # For deployment to Vercel(optional)







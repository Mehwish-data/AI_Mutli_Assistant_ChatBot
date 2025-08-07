
﻿#  𝐀𝐈_𝐌𝐮𝐥𝐭𝐢_𝐀𝐬𝐬𝐢𝐬𝐭𝐞𝐧𝐭_𝐁𝐨𝐭
 
Multi-Source AI Chatbot (Flask + Groq LLM + Custom Embeddings).A full-stack AI-powered chatbot that answers questions from PDFs, YouTube videos, websites, and raw text inputs** — built with Python, Flask, and blazing-fast Groq LLM.

 𝐊𝐞𝐲 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬

- 📄 **PDF Upload & Q&A**: Extracts text, generates embeddings, and allows intelligent querying
- 📺 **YouTube Video Bot**: Transcribes video content using Whisper and supports Q&A
- 🌐 **Website Scraper**: Extracts clean website content for question answering
- ✍️ **Raw Text Upload**: Directly input text for embedding and querying
- ⚡ **Groq LLM API**: Ultra-low latency responses via Groq’s OpenAI-compatible API
- 🔍 **Semantic Search**: Powered by SentenceTransformer + FAISS

---

 🧱 𝐓𝐞𝐜𝐡 𝐒𝐭𝐚𝐜𝐤

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

├── requirements.txt

└── vercel_wsai.py # For deployment to Vercel(optional)

𝐂𝐫𝐞𝐚𝐭𝐞 𝐚𝐧𝐝 𝐚𝐜𝐭𝐢𝐯𝐚𝐭𝐞 𝐞𝐧𝐯𝐢𝐫𝐨𝐧𝐦𝐞𝐧𝐭

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

𝐈𝐧𝐬𝐭𝐚𝐥𝐥 𝐝𝐞𝐩𝐞𝐧𝐝𝐞𝐧𝐜𝐢𝐞𝐬
 
pip install -r requirements.txt
 
𝐂𝐫𝐞𝐚𝐭𝐞 𝐚.𝐞𝐧𝐯 𝐟𝐢𝐥𝐞 𝐢𝐧 𝐭𝐡𝐞 𝐁𝐚𝐜𝐤𝐞𝐧𝐝/ 𝐟𝐨𝐥𝐝𝐞𝐫:

GROQ_API_KEY=your_groq_api_key_here

𝐑𝐮𝐧 𝐭𝐡𝐞 𝐅𝐥𝐚𝐬𝐤 𝐚𝐩𝐩

python app.py

Then open your browser to: http://localhost:5000

𝐀𝐏𝐈 𝐌𝐨𝐝𝐮𝐥𝐞𝐬 & 𝐑𝐨𝐮𝐭𝐞𝐬

Each bot is organized as a modular file inside the bots/ directory:

| Module           | Description                       |
| ---------------- | --------------------------------- |
| `pdf_bot.py`     | Upload PDFs and query via LLM     |
| `text_bot.py`    | Process user input text           |
| `youtube_bot.py` | Handle YouTube transcription/Q\&A |
| `website_bot.py` | Scrape and query website content  |

Supporting logic is organized under:

📁 embeddings/: Chunking, vectorization, and indexing

📁 utils/: Shared utilities for processing and transcription

📁 templates/: Frontend UI (index.html)

𝐄𝐱𝐚𝐦𝐩𝐥𝐞 𝐔𝐬𝐞 𝐂𝐚𝐬𝐞𝐬

Academic search in long PDFs and YouTube lectures

Customer support for scraped product pages

Education/EdTech tools for video-based learning

Enterprise Q&A over internal documents or URLs

👩‍💻 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐛𝐲

𝐌𝐞𝐡𝐰𝐢𝐬𝐡 𝐔𝐦𝐚𝐫

AI Engineer and Data Analyst 

🙌 𝐀𝐜𝐤𝐧𝐨𝐰𝐥𝐞𝐝𝐠𝐞𝐦𝐞𝐧𝐭𝐬

Groq API

SentenceTransformers

FAISS

OpenAI Whisper













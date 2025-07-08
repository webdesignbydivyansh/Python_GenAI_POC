# 🏆 Python GenAI POC – Personalized Sports Highlights Portal

This is a full-stack AI-powered application that generates personalized sports highlight videos using LLM-generated summaries, player images, and text-to-speech audio — all combined into a video and uploaded to Google Cloud Storage (GCS).

🚀 Built with:
- **Frontend**: Next.js 15 + Tailwind CSS
- **Backend**: FastAPI + MoviePy + gTTS + GCS
- **LLM Model**: Ollama (LLaMA3 running locally)
- **Video Hosting**: Google Cloud Storage

---

## 🔍 Features

- 🧠 Uses local LLM (`llama3`) to generate player summaries
- 🖼️ Fetches player images using [TheSportsDB API](https://www.thesportsdb.com/)
- 🔊 Converts summaries to speech with `gTTS`
- 🎥 Generates highlight videos with `moviepy`
- ☁️ Uploads videos to GCS and provides public video links
- 🌐 Interactive frontend search interface for player names

---

## 📁 Project Structure

Python_GenAI_POC/
├── backend/ # FastAPI server
│ ├── main.py # API entry point
│ ├── fetchImage.py # Image fetch logic
│ ├── generateText.py # LLM summary
│ ├── videoGeneration.py # MoviePy video builder
│ ├── videoUpload.py # Upload to GCS
│ └── ...
├── frontend/ # Next.js frontend
│ ├── src/
│ │ └── app/
│ │ ├── page.tsx
│ │ └── player/[name]/page.tsx
│ └── components/
│ └── SearchBar.tsx
└── README.md

## 🛠️ Setup

### ✅ Backend (FastAPI)

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
Make sure:

Ollama is running: ollama serve
GCS credentials (key.json) are set up
Bucket is publicly accessible

✅ Frontend (Next.js)
cd frontend
npm install
npm run dev
Access app at: http://localhost:3000

📦 Environment Variables

Backend 
GOOGLE_APPLICATION_CREDENTIALS=key.json
BUCKET_NAME=your-gcs-bucket
OLLAMA_URL=http://localhost:11434

🌐 API Endpoint

POST /api/video
Body: { "player": "ms dhoni" }

Response:
{
  "video_url": "https://storage.googleapis.com/your-bucket/player_name.mp4"
}

📌 Credits

Built by Divyansh Kushwaha
Uses OpenAI-compatible LLMs via Ollama
Thanks to TheSportsDB for image API
🧠 Future Ideas

Add user accounts and saved video history
Enable video customization (theme, voice, transitions)
Support team highlights instead of individual players
Deploy on Vercel / Render / GCP Cloud Run

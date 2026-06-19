from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import chat

# Create FastAPI app instance
app = FastAPI(
    title="NexusAI Support Bot API",
    description="Backend API for NexusAI multi-agent customer support bot",
    version="0.1.0"
)

# ── CORS Middleware ─────────────────────────────────────
# Allows React frontend (port 5173) to talk to
# this FastAPI backend (port 8000)

# Without this the browser blocks all requests

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Routes ──────────────────────────────────────────────

@app.get("/health")
def health():
    """Health check - confirms server is running"""
    return {"status": "ok", "message": "NexusAI backend is live"}


# Include chat router
# Adds all routes from app/routers/chat.py
app.include_router(chat.router)
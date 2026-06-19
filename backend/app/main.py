from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.upload import router as upload_router
from app.routers.chat import router as chat_router


app = FastAPI(
    title="NexusAI Support Bot API",
    description="Multi-agent customer support backend",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router)
app.include_router(chat_router)


@app.get("/")
def home():
    return {"message": "Welcome to AgentDesk API"}


@app.get("/health")
def health():
    return {
        "status": "ok",
        "message": "NexusAI backend is live",
    }
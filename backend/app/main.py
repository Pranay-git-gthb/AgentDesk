from fastapi import FastAPI
from app.routes.upload import router as upload_router

app = FastAPI()

app.include_router(upload_router)


@app.get("/")
def home():
    return {"message": "Welcome to AgentDesk API"}

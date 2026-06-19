from fastapi import APIRouter

router = APIRouter()


@router.post("/chat")
def chat():
    """
    Week 2 - Dummy chat endpoint.

    Returns hardcoded response for now.
    Will connect to LLM in Week 3.
    """
    reply_text = (
        "Hello! I am the NexusAI Support Bot."
        " How can I help you today?"
    )
    return {"reply": reply_text}

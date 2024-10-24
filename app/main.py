from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.models.chat import ChatRequest, ChatResponse
from app.services.groq_chatbot_service import get_groq_chatbot_response

app = FastAPI()

# Serve static files from the frontend directory
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

# Chatbot endpoint
@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    response = get_groq_chatbot_response(request.user_message)
    return ChatResponse(response=response)

# Serve the HTML file at the root URL
@app.get("/", response_class=HTMLResponse)
def read_root():
    try:
        with open("frontend/index.html") as f:
            return HTMLResponse(content=f.read())
    except FileNotFoundError:
        return HTMLResponse(content="Index file not found.", status_code=404)

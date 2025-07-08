from fastapi import FastAPI
from pydantic import BaseModel
from utils.modele import get_response

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.get("/")
async def root():
    return {"message": "FastAPI running. Use POST /process-text/ to interact."}

@app.post("/process-text/")
async def process_text(req: TextRequest):
    response = get_response(req.text)
    return {"response": response}

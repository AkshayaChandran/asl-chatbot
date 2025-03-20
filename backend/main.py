from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from asl_converter import get_asl_image  # Import function from asl_converter.py

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextRequest(BaseModel):
    text: str

@app.post("/convert_to_asl")
async def convert_to_asl(request: TextRequest):
    asl_image_url = get_asl_image(request.text)

    if asl_image_url:
        return {"asl_images": [asl_image_url]}
    else:
        raise HTTPException(status_code=404, detail="ASL translation not found")

@app.get("/")
async def root():
    return {"message": "ASL Chatbot Backend is Running!"}  # ✅ Fixed string error

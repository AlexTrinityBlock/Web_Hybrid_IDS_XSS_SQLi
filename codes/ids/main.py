from typing import Union
from fastapi import FastAPI
from ids_model import IDSModel
from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Cors
app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Load model
model = IDSModel()

# Text model
class InputText(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "This is the IDS API"}

@app.post("/detect/")
def detect(text: InputText,response: Response):
    if len(text.text) > 1000:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": "Text is too long"}    
    result = model.predict(text.text)    
    return result
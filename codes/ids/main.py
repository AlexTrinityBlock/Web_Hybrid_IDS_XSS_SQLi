from typing import Union
from fastapi import FastAPI
from controllers.ids_model_controller import IDSModelController
from controllers.gpt_model_controller import GPTModelController
from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
from api_format.ids_input_format import IDSInputFormat


# CORS
app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model
ids_model = IDSModelController()

# URLs
# root


@app.get("/", tags=["root"])
def read_root():
    return {"message": "This is the IDS API"}

# Detection SQL injection and XSS


@app.post("/detect/", tags=["ids"])
def detect(text: IDSInputFormat):
    result = ids_model.predict_attack_type(text.text)
    return result

# Call openai api

@app.post("/detect-gpt/", tags=["ids"])
def detect_gpt(text: IDSInputFormat):
    gpt_model = GPTModelController()
    result = gpt_model.predict_attack_type(text.text)
    return result

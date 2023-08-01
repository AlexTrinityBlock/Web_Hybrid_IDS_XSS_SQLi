from typing import Union
from fastapi import FastAPI
from controllers.hybrid_model_controller import IDSModelController
from controllers.gpt_model_controller import GPTModelController
from controllers.local_model_controller import LocalModelController
from controllers.log_controller import LogController
from models.create_tables import create_tables
from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
from api_format.ids_input_format import IDSInputFormat
from tensorflow import keras
import os
import time

# Set Python Timezone
time.tzset()

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
dir_path = os.path.dirname(os.path.realpath(__file__))
model = keras.models.load_model(
    dir_path+"/ml_models/model.h5")
ids_model = IDSModelController(model)
local_model = LocalModelController(model)

# Init database
create_tables()

# URLs

# Root URL


@app.get("/", tags=["root"])
def read_root():
    return {"message": "This is the IDS API"}

# Detection SQL injection and XSS with hybrid model


@app.post("/detect/hybrid", tags=["ids"])
def detect(text: IDSInputFormat):
    result = ids_model.predict_attack_type(
        text=text.text, from_ip=text.from_ip)
    return result

# Detection SQL injection and XSS with openai api gpt


@app.post("/detect/gpt/", tags=["ids"])
def detect_gpt(text: IDSInputFormat):
    gpt_model = GPTModelController()
    result = gpt_model.predict_attack_type(
        input_text=text.text, from_ip=text.from_ip)
    return result

# Detection SQL injection and XSS with local model


@app.post("/detect/local/", tags=["ids"])
def detect_local(text: IDSInputFormat):
    result = local_model.predict_attack_type(
        text=text.text, from_ip=text.from_ip)
    return result

# Read logs


@app.get("/logs", tags=["logs"])
def read_logs():
    log_controller = LogController()
    logs = log_controller.read_logs()
    return logs

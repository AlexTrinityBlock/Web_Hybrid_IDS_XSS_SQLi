from typing import Union
from fastapi import FastAPI, Query
from controllers.hybrid_model_controller import IDSModelController
from controllers.gpt_model_controller import GPTModelController
from controllers.local_model_controller import LocalModelController
from controllers.log_controller import LogController
from controllers.log_analysis_controller import LogAnalysisController
from models.create_tables import create_tables
from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
from api_format.ids_input_format import IDSInputFormat
from tensorflow import keras
import os
import time
from datetime import datetime, timedelta
from utils.encode_utils import encode_payload_decode

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

# Introduction URL


@app.get("/", tags=["Introduction"])
def read_root():
    return {"message": "This is the IDS API"}

# Detection SQL injection and XSS with hybrid model


@app.post("/detect/hybrid/", tags=["IDS"])
def detect(text: IDSInputFormat):
    payload_decode = encode_payload_decode(text.text)
    result = ids_model.predict_attack_type(
        text=payload_decode, from_ip=text.from_ip)
    return result

# Detection SQL injection and XSS with openai api gpt


@app.post("/detect/gpt/", tags=["IDS"])
def detect_gpt(text: IDSInputFormat):
    payload_decode = encode_payload_decode(text.text)
    gpt_model = GPTModelController()
    result = gpt_model.predict_attack_type(
        input_text=payload_decode, from_ip=text.from_ip)
    return result

# Detection SQL injection and XSS with local model


@app.post("/detect/local/", tags=["IDS"])
def detect_local(text: IDSInputFormat):
    payload_decode = encode_payload_decode(text.text)
    result = local_model.predict_attack_type(
        text=payload_decode, from_ip=text.from_ip)
    return result

# Analysis logs by GPT


@app.get("/logs/analysis/", tags=["Analysis"])
def log_analysis():
    log_analysis_controller = LogAnalysisController()
    result = log_analysis_controller.gpt_analysis()
    return result

# Analysis logs by GPT cache


@app.get("/logs/analysis/cached/", tags=["Analysis"])
def log_analysis_cache():
    log_analysis_controller = LogAnalysisController()
    result = log_analysis_controller.get_analysis_cache()
    return result


# Read logs


@app.get("/logs/", tags=["Log"])
def read_logs(
    start_time: str | None = Query(
        default=(datetime.now()-timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"), max_length=20),
    end_time: str | None = Query(
        default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), max_length=20)
):
    start_time_obj: datetime
    end_time_obj: datetime
    try:
        start_time_obj = datetime.strptime(
            start_time, '%Y-%m-%d %H:%M:%S')
        end_time_obj = datetime.strptime(
            end_time, '%Y-%m-%d %H:%M:%S')
    except Exception as e:
        return {"message": str(e)}

    log_controller = LogController()
    logs = log_controller.read_logs(start_time_obj, end_time_obj)
    return logs

# Count positives, negatives and total of logs


@app.get("/logs/statistics/", tags=["Log"])
def statistics_total_logs():
    log_controller = LogController()
    logs = log_controller.read_statistics_total()
    return logs

# Get lasthour logs


@app.get("/logs/lasthour/", tags=["Log"])
def lasthour_logs():
    log_controller = LogController()
    logs = log_controller.read_last_hours_access()
    return logs

# Read logs by id range


@app.get("/logs/id_range/", tags=["Log"])
def read_logs_by_id_range(
    start_id: int = Query(default=1, ge=0),
    end_id: int = Query(default=3, ge=0)
):
    log_controller = LogController()
    logs = log_controller.read_logs_by_id_range(start_id, end_id)
    return logs

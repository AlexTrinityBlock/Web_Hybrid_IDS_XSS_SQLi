from models.log_model import LogModel
from models.base import SessionLocal
import datetime

class LogController:
    def __init__(self):
        self.db = SessionLocal()

    def create_log(self, model_type: str,
                   result: str,
                   payload: str,
                   is_positive: bool = None,
                   SQLi_probability: float = None,
                   XSS_probability: float = None, Benign_probability: float = None,
                   raw_gpt_response: str = None,
                   from_ip:str = None,
                   ):
        log_model = LogModel(is_positive=is_positive,
                             SQLi_probability=SQLi_probability,
                             XSS_probability=XSS_probability,
                             Benign_probability=Benign_probability,
                             model_type=model_type,
                             result=result,
                             payload=payload,
                             raw_gpt_response=raw_gpt_response,
                             from_ip=from_ip,
                             )
        print("Add model to DB")
        self.db.add(log_model)

        print("Commit model to DB")
        self.db.commit()

        print("Refresh model from DB")
        self.db.refresh(log_model)
        return True
    
    def read_logs(self, start_time: datetime = None, end_time: datetime = None):
        query = self.db.query(LogModel)
        if start_time:
            query = query.filter(LogModel.timestamp >= start_time)
        if end_time:
            query = query.filter(LogModel.timestamp <= end_time)
        return query.all()

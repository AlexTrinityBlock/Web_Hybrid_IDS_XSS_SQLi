from models.log_model import LogModel
from models.base import SessionLocal


class LogController:
    def __init__(self):
        self.db = SessionLocal()

    def create_log(self, model_type: str,
                   result: str,
                   is_positive: bool = None,
                   SQLi_probability: float = None,
                   XSS_probability: float = None, Benign_probability: float = None,
                   raw_gpt_response: str = None
                   ):
        log_model = LogModel(is_positive=is_positive,
                             SQLi_probability=SQLi_probability,
                             XSS_probability=XSS_probability,
                             Benign_probability=Benign_probability,
                             model_type=model_type,
                             result=result,
                             raw_gpt_response=raw_gpt_response,
                             )
        print("Add model to DB")
        self.db.add(log_model)

        print("Commit model to DB")
        self.db.commit()

        print("Refresh model from DB")
        self.db.refresh(log_model)
        return True

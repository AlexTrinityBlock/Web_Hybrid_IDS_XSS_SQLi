from datetime import datetime
from pydantic import BaseModel

class LogsTimeRangeFormat(BaseModel):
    start_time: datetime = None
    end_time: datetime = None
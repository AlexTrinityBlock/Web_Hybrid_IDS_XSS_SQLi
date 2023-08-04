from models.log_model import LogModel
from models.base import SessionLocal
import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class LogController:
    def __init__(self):
        self.db = SessionLocal()

    def __del__(self):
        self.db.close()
        print("Close session Class del")

    def create_log(self, model_type: str,
                   result: str,
                   payload: str,
                   is_positive: bool = None,
                   SQLi_probability: float = None,
                   XSS_probability: float = None, Benign_probability: float = None,
                   raw_gpt_response: str = None,
                   from_ip: str = None,
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
        with self.db as session:
            session.add(log_model)
            session.commit()
            session.refresh(log_model)
        return True

    def read_logs(self, start_time: datetime = None, end_time: datetime = None):
        with self.db as session:
            query = session.query(LogModel)
            if start_time:
                query = query.filter(LogModel.timestamp >= start_time)
            if end_time:
                query = query.filter(LogModel.timestamp <= end_time)
            result = query.all()
        return result

    def read_statistics_total(self):
        with self.db as session:
            # Count total positive number of log
            query = session.query(LogModel)
            query = query.filter(LogModel.is_positive == 'true')
            positive_number: int = query.count()

            # Coount total negative number of log
            query = self.db.query(LogModel)
            query = query.filter(LogModel.is_positive == 'false')
            negative_number: int = query.count()

            # Coount total number of log
            query = self.db.query(LogModel)
            total_number: int = query.count()

        result = {
            'positive_number': positive_number,
            'negative_number': negative_number,
            'total_number': total_number,
        }

        return result

    def read_last_hours_access(self):
        with self.db as session:
            # Init
            query = session.query(LogModel)
            query = query.filter(
                LogModel.timestamp >= datetime.datetime.now() - datetime.timedelta(hours=1))
            log_result: list = query.all()

        # I need to get a list of time log for line chart
        positive_time_log_list: list = []
        negative_time_log_list: list = []
        unknown_time_log_list: list = []

        # Init list with 60 minutes in one hour
        for i in range(60):
            positive_time_log_list.append(0)
            negative_time_log_list.append(0)
            unknown_time_log_list.append(0)

        # Count positive number every minute
        for log in log_result:
            on_minute: int = self.__happenTime(log.timestamp)
            if log.is_positive == True:
                positive_time_log_list[on_minute] += 1
            elif log.is_positive == False:
                negative_time_log_list[on_minute] += 1
            else:
                unknown_time_log_list[on_minute] += 1

        return {
            "positive_time_log_list": positive_time_log_list,
            "negative_time_log_list": negative_time_log_list,
            "unknown_time_log_list": unknown_time_log_list,
            "timeline": self.__timelineBuilder(),
        }

    def __happenTime(self, time: datetime.datetime) -> int:
        now = datetime.datetime.now()
        relativeTime = now - time
        on_minute_str: str = str(relativeTime).split(':')[1]
        on_minute: int = int(on_minute_str)
        return on_minute

    def __timelineBuilder(self) -> list:
        temp = datetime.datetime.now()
        timeline: list = []

        for i in range(60):
            temp = temp - datetime.timedelta(minutes=1)
            temp_minute_str: str = str(temp).split(':')[1]
            if temp_minute_str[1] == '0':
                temp_minute_str = temp_minute_str[0]
                timeline.append(temp_minute_str+'0')
            else:
                timeline.append('')
        return timeline
    
    def read_logs_by_id_range(self, start_id: int, end_id: int):
        with self.db as session:
            logs = session.query(LogModel).filter(LogModel.id >= start_id, LogModel.id <= end_id).all()
        return logs
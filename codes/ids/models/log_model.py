from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float
from models.base import Base, engine
import datetime


class LogModel(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True, index=True,
                unique=True, autoincrement=True)
    is_positive = Column(Boolean, nullable=True)
    payload = Column(String, nullable=False)
    SQLi_probability = Column(Float, nullable=True)
    XSS_probability = Column(Float, nullable=True)
    Benign_probability = Column(Float, nullable=True)
    model_type = Column(String, nullable=False)
    result = Column(String, nullable=False)
    raw_gpt_response = Column(String, nullable=True)
    from_ip = Column(String, nullable=True)
    timestamp = Column(DateTime, default=datetime.datetime.now)

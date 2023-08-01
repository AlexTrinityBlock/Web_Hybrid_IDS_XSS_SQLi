from models.log_model import LogModel
from models.base import engine

def create_tables():
    log = LogModel()
    log.metadata.create_all(engine)
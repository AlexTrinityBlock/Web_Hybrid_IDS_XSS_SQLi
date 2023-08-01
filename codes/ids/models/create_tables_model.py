from models.log_model_base import Log
from models.base import engine

log = Log()
log.metadata.create_all(engine)
from models.log_model import LogModel
from models.base import engine
from controllers.log_controller import LogController
from controllers.log_analysis_controller import LogAnalysisController
from sqlalchemy import inspect, create_engine


def create_tables():
    log = LogModel()
    if not inspect(engine).has_table('logs'):  # If table don't exist, Create.
        log = LogModel()
        log.metadata.create_all(engine)
        log_controller = LogController()
        log_controller.create_log(
            'Init',
            'False',
            'Hello world',
            from_ip='127.0.0.1',
            is_positive=False,
        )
        log_analysis_controller = LogAnalysisController()
        log_analysis_controller.saving_cache('Hi, please press update data!')

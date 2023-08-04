from controllers.log_controller import LogController
import json
from datetime import datetime, timedelta
from sqlalchemy import inspect

prompt_1 = """
This is my system logs, please analyze the security issues and give suggestions
"""

sysyem_prompt_1 = """
Please act as a system security advisor, and tell me that some IPs need attention.
"""


def get_logs(query_obj):
    result = []
    for item in query_obj:
        result.append(object_as_dict(item))
    return json.dumps(result, default=str)


def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}


def get_prompt():
    before = (datetime.now()-timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_controller = LogController()
    statistics_logs = json.dumps(log_controller.read_statistics_total())
    logs_obj = log_controller.read_logs(before, now)
    logs_str = get_logs(logs_obj)
    result = (prompt_1 + statistics_logs + logs_str)[0:3000]
    return result


def get_system_prompt():
    return sysyem_prompt_1

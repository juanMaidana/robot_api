from robot_logs.robot_logger import write_log
from object_management.string.function_log_table import function_log_table
from object_management.json.json_reader import json_reader
from os.path import join, realpath, dirname
from json import dumps
from simplejson import JSONDecodeError

config = json_reader(join(dirname(realpath(__file__)), 'logs_config.json'))


def print_logs(level=config.get("default_level"), html=config.get("html")):
    """Generic decorator to print function and in params on logs.

    :param level: log level, by default on logs_config.json.
    :param html: messages are html, by default on logs_config.json.
    :return: logs for function name, params and values.
    """
    def decorator(function):
        def wrapper(*args, **kwargs):
            write_log(function_log_table(html, function, *args, **kwargs),
                      level=level, html=html)
            result = function(*args, **kwargs)
            write_log(config.get("messages").get("success") + function.__name__,
                      level="INFO", html=False)
            if result:
                write_log("Result: " + str(result), level=level, html=html)
            return result
        return wrapper
    return decorator


def print_api_logs(level=config.get("default_level"), html=config.get("html")):
    """API function decorator to print function and in params on logs.

    The function should return the status code and the response body.
    :param level: log level, by default on logs_config.json.
    :param html: messages are html, by default on logs_config.json.
    :return: logs for function name, params, value, status and response body.
    """
    def decorator(function):
        def wrapper(*args, **kwargs):
            write_log(function_log_table(html, function, *args, **kwargs),
                      level=level, html=html)
            status, response = function(*args, **kwargs)
            write_log('Status: ' + status, level=level, html=html)
            try:
                write_log('Response: ' + dumps(response, indent=4),
                          level=level, html=html)
            except JSONDecodeError:
                write_log(config.get("messages").get("unreadable"),
                          level=level, html=html)
            write_log(config.get("messages").get("success") + function.__name__,
                      level="INFO", html=False)
            return status
        return wrapper
    return decorator

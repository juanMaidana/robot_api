from robot.output import librarylogger
from robot.running.context import EXECUTION_CONTEXTS
from object_management.json.json_reader import json_reader
from os.path import join, realpath, dirname

config = json_reader(join(dirname(realpath(__file__)), 'logs_config.json'))


def write_log(msg, level=config.get("default_level"), html=config.get("html")):
    """Works as a print but on robot logs reports."""
    if EXECUTION_CONTEXTS.current is not None:
        librarylogger.write(msg, level, html)

from core.libraries.my_library import *
from pivotal_tracker.utils.pivotal_request import PivotalRequest
from pivotal_tracker.utils.context import Context
from core.utils.json_reader import json_reader
from os.path import join, realpath, dirname
from json import dumps

context = Context()
config = json_reader(join(dirname(realpath(__file__)),
                          '..', 'config.json'))
endpoints = json_reader(join(dirname(realpath(__file__)),
                             '..', 'endpoints.json'))


def log_in_api(user):
    context.api = PivotalRequest()
    context.username = user


def do_user_request(http_type, endpoint_name, data):
    context.api.build_end_point(config["base_url"] + endpoints[endpoint_name])
    context.headers = {
        config["headers"]["token"]: config["users"][context.username]["token"],
        config["headers"]["contents"]: "application/json",
    }
    data = dumps(data) if data else data
    context.api.do_request(http_type, context.headers, data=data)


def do_request(http_type, endpoint_name, username, data):
    context.api = PivotalRequest()
    context.api.build_end_point(config["base_url"]+endpoints[endpoint_name])
    context.headers = {
        config["headers"]["token"]: config["users"][username]["token"],
        config["headers"]["contents"]: "application/json",
    }
    data = dumps(data) if data else data
    context.api.do_request(http_type, context.headers, data=data)


def get_status_code():
    return context.api.get_status()


def get_response():
    return context.api.get_json()


def get_from_response(key):
    return context.api.get_json().get(key)

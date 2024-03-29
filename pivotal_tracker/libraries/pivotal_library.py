from pivotal_tracker.pivotal_request.pivotal_request import PivotalRequest
from pivotal_tracker.context.context import Context
from object_management.json.json_reader import json_reader
from json import dumps
from datetime import datetime
from object_management.string.prepare_string import prepare_string
from os.path import join, realpath, dirname
from robot_logs.robot_decorators import print_api_logs

context = Context()
config = json_reader(join(dirname(realpath(__file__)),
                          '..', 'config.json'))
endpoints = json_reader(join(dirname(realpath(__file__)),
                             '..', 'endpoints.json'))


def request(http_type, data):
    data = dumps(data) if data else ''
    data = prepare_string(data, config["prefix"], datetime.now().
                          strftime("%m-%d-%Y_%H:%M:%S"))
    context.api.do_request(http_type, context.headers, data=data)
    return context.api.get_status(), context.api.get_json()


def log_in_api(user):
    """Sets api and username attributes on context.

    :param user: must be on config file.
    :return: exit code 0.
    """
    context.api = PivotalRequest()
    context.username = user


@print_api_logs()
def send_user_request(http_type, endpoint_name, data):
    """Does an http request given an endpoint key and data.

    * This function assumes the username is already set on context.
    :param http_type: GET, POST, PUT, DELETE.
    :param endpoint_name: must be on endpoints.json.
    :param data: data for the request (must be a dict).
    :return: exit code 0.
    """
    context.api.build_end_point(config["base_url"] + endpoints[endpoint_name])
    context.headers = {
        config["headers"]["token"]: config["users"][context.username]["token"],
        config["headers"]["contents"]: "application/json",
    }
    return request(http_type, data)


@print_api_logs()
def send_request(http_type, endpoint_name, username, data):
    """Does an http request given an endpoint key and data.

    :param http_type: GET, POST, PUT, DELETE.
    :param endpoint_name: must be on endpoints.json.
    :param username: the user on config file to do the request.
    :param data: data for the request (must be a dict).
    :return: exit code 0.
    """
    context.api = PivotalRequest()
    context.api.build_end_point(config["base_url"]+endpoints[endpoint_name])
    context.headers = {
        config["headers"]["token"]: config["users"][username]["token"],
        config["headers"]["contents"]: "application/json",
    }
    return request(http_type, data)


def get_status_code():
    """Get status code of API attribute."""
    return context.api.get_status()


def get_response():
    """Get response as json of API attribute."""
    return context.api.get_json()


def get_from_response(key):
    """Get a specific part of the response based on key."""
    return context.api.get_json().get(key)

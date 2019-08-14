from pivotal_tracker.utils.pivotal_request import PivotalRequest
from core.utils.json_reader import json_reader
from os.path import join, realpath, dirname

config = json_reader(join(dirname(realpath(__file__)), '..', 'config.json'))
endpoints = json_reader(join(dirname(realpath(__file__)), '..', 'endpoints.json'))

ROBOT_LISTENER_API_VERSION = 2


def end_suite(name, attrs):
    api = PivotalRequest()
    headers = {
        config["headers"]["token"]: config["users"]["owner"]["token"],
        config["headers"]["contents"]: "application/json",
    }
    api.build_end_point(config["base_url"] + endpoints["projects"])
    api.do_request('GET', headers)
    projects = api.get_json()
    for item in projects:
        if "viper" in item["name"]:
            api.build_end_point(config["base_url"] + endpoints["project"], item["id"])
            api.do_request('DELETE', headers)


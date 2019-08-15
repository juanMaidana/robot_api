from pivotal_tracker.utils.pivotal_request import PivotalRequest
from core.utils.json_reader import json_reader
from os.path import join, realpath, dirname

config = json_reader(join(dirname(realpath(__file__)),
                          '..', 'config.json'))
endpoints = json_reader(join(dirname(realpath(__file__)),
                             '..', 'endpoints.json'))

ROBOT_LISTENER_API_VERSION = 2


def delete_objects(generic_tag, specific):
    api = PivotalRequest()
    headers = {
        config["headers"]["token"]: config["users"]["owner"]["token"],
        config["headers"]["contents"]: "application/json",
    }
    api.build_end_point(config["base_url"] + endpoints[generic_tag])
    api.do_request('GET', headers)
    projects = api.get_json()
    for item in projects:
        if config.get("prefix") in item["name"]:
            api.build_end_point(config["base_url"] + endpoints[specific], item["id"])
            api.do_request('DELETE', headers)


def end_suite(name, attrs):
    delete_objects("projects", "project")
    delete_objects("workspaces", "workspace")


def start_suite(name, attrs):
    delete_objects("projects", "project")
    delete_objects("workspaces", "workspace")

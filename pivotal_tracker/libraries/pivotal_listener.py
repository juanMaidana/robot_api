from pivotal_tracker.pivotal_request.pivotal_request import PivotalRequest
from object_management.json.json_reader import json_reader
from os.path import join, realpath, dirname

config = json_reader(join(dirname(realpath(__file__)),
                          '..', 'config.json'))
endpoints = json_reader(join(dirname(realpath(__file__)),
                             '..', 'endpoints.json'))

ROBOT_LISTENER_API_VERSION = 2


def delete_objects(generic_tag, specific):
    """Delete objects on pivotal tracker.

    :param generic_tag: used to get all objects.
    :param specific: used to delete objects by id.
    :return: exit code 0.
    """
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
            api.build_end_point(config["base_url"] +
                                endpoints[specific], item["id"])
            api.do_request('DELETE', headers)


def start_suite(name, attrs):
    """At the start of the execution delete objects."""
    delete_objects("projects", "project")
    delete_objects("workspaces", "workspace")


def end_suite(name, attrs):
    """At the end of the execution delete objects."""
    delete_objects("projects", "project")
    delete_objects("workspaces", "workspace")

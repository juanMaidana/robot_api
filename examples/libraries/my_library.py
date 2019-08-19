from os.path import join, realpath, dirname

service_options = {
    "LINUX": ["mysql:5.7", "wordpress:latest"],
    "WINDOWS": ["mysql:5.7", "wordpress:latest"],
    "OTHER": ["mysql:5.7", "wordpress:latest"]
}


def join_two_strings(arg1, arg2):
    """Takes two strings and joins them."""
    return arg1 + " " + arg2


def get_project_path():
    """Using os library return the current project path"""
    return join(dirname(realpath(__file__)), '..', '..')


def get_operating_system(environment_variables):
    """Attempts to recognize the OS.

    :param: environment_variables, dict or map of variables.
    :returns: OS name recognized.
    """
    if "SHELL" in environment_variables:
        return "LINUX"
    else:
        return "OTHER"


def prepare_contents(operating_system, raw_data):
    """Multiple operating systems might use different images.

    Values will be replaced according to the service options map.
    :param operating_system: (uppercase) can be linux, windows, other.
    :param raw_data: data with values to be replaced.
    :return: data with values replaced.
    """
    replacer = service_options[operating_system]
    return raw_data.replace("${VAL_0}", replacer[0]).replace("${VAL_1}", replacer[1])

from os.path import join, realpath, dirname

service_options = {
    "LINUX": ["mysql:5.7", "wordpress:latest"],
    "WINDOWS": ["mysql:5.7", "wordpress:latest"]
}


def join_two_strings(arg1, arg2):
    return arg1 + " " + arg2


def get_project_path():
    return join(dirname(realpath(__file__)), '..', '..')


def get_operating_system(environment_variables):
    if "DESKTOP_SESSION" in environment_variables:
        return "LINUX"
    elif "OS" in environment_variables:
        return "WINDOWS"


def prepare_contents(operating_system, raw_data):
    replacer = service_options[operating_system]
    return raw_data.replace("${VAL_0}", replacer[0]).replace("${VAL_1}", replacer[1])

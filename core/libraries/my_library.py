from os.path import join, realpath, dirname


def join_two_strings(arg1, arg2):
    return arg1 + " " + arg2


def get_project_path():
    return join(dirname(realpath(__file__)), '..', '..')

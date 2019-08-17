import os
from os.path import join, realpath, dirname
from object_management.json.json_reader import json_reader

setup = json_reader(join(dirname(realpath(__file__)), 'setup.json'))

command = ["python -m robot"]

args = []
for config in setup:
    if setup[config] and config != "(test_cases)":
        args.append("--" + config + " " + setup[config])

os.system(' '.join(command + args + [setup["(test_cases)"]]))

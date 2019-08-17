import os
from os.path import join, realpath, dirname
from object_management.json.json_reader import json_reader

setup = json_reader(join(dirname(realpath(__file__)), 'setup.json'))

command = [setup.get("python_version"), "-m robot"]

args = []
for config in setup.get("args"):
    if setup.get("args")[config]:
        args.append("--" + config + " " + setup.get("args")[config])
print(' '.join(command + args + [setup["test_cases"]]))
os.system(' '.join(command + args + [setup["test_cases"]]))

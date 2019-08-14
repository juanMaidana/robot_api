from json import loads


def json_reader(file_path):
    f = open(file_path)
    json = loads(f.read())
    f.close()
    return json

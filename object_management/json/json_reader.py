from json import loads


def json_reader(file_path):
    """Read a .json file.

    :param file_path, the full path of the .json file.
    Open the file, reads its contents.
    :returns dict object with the contents.
    """
    f = open(file_path)
    json = loads(f.read())
    f.close()
    return json

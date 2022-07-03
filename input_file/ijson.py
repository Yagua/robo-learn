from sys import exit
import json

#unpack json object
def unpack_object(data):
    """
    it admits any kind of values exept other objects.
    if it finds a dict-based vale, that content will be skiped
    """
    result = {}
    for key, val in data.items():
        if type(val) == dict: continue
        elif type(val) == list:
            str_list = ""
            for item in val:
                str_list += f"{item}\n"
            result[key] = str_list
        else:
            result[key] = str(val)
    return result

# read json file and return it's content
def read_json(home, file):
    try:
        path = f"{home}/{file}.json"
        if home == None: path = file
        json_file = open(path)
        data = json.load(json_file)
        json_file.close()
        return unpack_object(data)
    except(FileNotFoundError):
        print("[Error]: File not Found")
        exit(1)
    except(json.decoder.JSONDecodeError):
        print("[Error]: Bad JSON format in file", file)
        exit(1)


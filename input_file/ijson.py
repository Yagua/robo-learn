import utils
import json

def unpack_object(data):
    result = []
    for k in data:
        result.append(data[k])
    return result

def read_json(file, home):
    try:
        path = "%s/%s.json" %(home, file)
        json_file = open(path)
        data = json.load(json_file)
        return unpack_object(data)
    except(FileNotFoundError):
        print("[Error]: File not Found")
        utils.sys_exit()

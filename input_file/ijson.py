import utils
import json

#unpack json object
def unpack_object(data):
    result = []
    for k in data:
        result.append(data[k])
    return result

#read json file and return it's content
def read_json(file, home):
    try:
        path = "%s/%s.json" %(home, file)
        if home == None: path = path = file
        json_file = open(path)
        data = json.load(json_file)
        return unpack_object(data)
    except(FileNotFoundError):
        print("[Error]: File not Found")
        utils.sys_exit()
    except(json.decoder.JSONDecodeError):
        print("[Error]: Bad JSON format in file", file)
        utils.sys_exit()

import json

impu = input("file: ")
with open("/home/yagua/.config/scripts/robo-learn/lists/%s.json" % (impu)) as json_file:
    data = json.load(json_file)
    for k in data :
        print(data[k])


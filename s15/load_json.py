
import json

with open("json_data.json",'r') as fp:
    # json.dump(a,fp)
    a = json.load(fp)

print(a)
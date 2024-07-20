import json

a = {"name":"mohammad",
     "age":33,
     "gender":True,
     "course":None,
     "average":19.6,
     "grades":[19,16,10]}

with open("json_data.json",'a') as fp:
    json.dump(a,fp)
    # json.load

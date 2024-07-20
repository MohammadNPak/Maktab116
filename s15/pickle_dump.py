import pickle

a = {"name":"mohammad",
     "age":33,
     "gender":True,
     "course":None,
     "average":19.6,
     "grades":[19,16,10]}

with open("pickle_data.pkl","wb") as fp:
    pickle.dump(a,fp)

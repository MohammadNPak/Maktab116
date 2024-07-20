import pickle

with open("pickle_data.pkl","rb") as fp:
    a = pickle.load(fp)

print(a)
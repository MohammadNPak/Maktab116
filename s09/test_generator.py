# c = (x for x in range(1000))

# for i in c:
#     print(i)


def read_batch(file_address,batch_size):
    with open(file_address,'r',encoding="ascii", errors="surrogateescape") as fp:
        data = []
        for i in range(batch_size):
            data.append(fp.readline().split(","))
        yield data

address="Sample-Spreadsheet-5000-rows.csv"
file_generator = read_batch(address,8)

for i,d in enumerate(file_generator):
    print(d)
    if i>1:
        break


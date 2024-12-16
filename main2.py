with open("abc.txt") as fp:
    data1 = fp.read()

with open("xyz.txt") as fp:
    data2 = fp.read()

data1+="\n"
data1+=data2

print("merging")

with open("mering.txt","w")as fp:
    fp.write(data1)

data1.close()
data2.closed()
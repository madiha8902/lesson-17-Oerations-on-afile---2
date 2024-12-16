with open("abc.txt","w")as file:
    file.write("hello i am madiha")

with open("abc.txt","r")as file:
    data=file.readlines()
    print("all words")
    for line in data:
        word=line.split()
        print(word)

file.close()

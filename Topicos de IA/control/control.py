f = open("dataset.txt", "r")


data = f.read()
print(data)

Y=[]
for i in data:
    if i == ' ':
        continue
    else:
        Y.append(int(i));

print(Y)
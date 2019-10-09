f = open('file.txt','r')
message = f.read()
f.close()

array = message.split('\n')

newArray = []

for i in range(len(array)):
    if "text1" in array[i] and "text2" in array[i]:
        newArray.append(array[i])

o = open('output.txt','w')
for i in range(len(newArray)):
    o.write(newArray[i] + "\n")
o.close()

f = open('myfile.txt', 'r')
# text = f.read()
# print(text)


while True:
    line = f.readline()
    if not line:
        break
    print(line)

f.close()
dic = { 1:"one", 2:"two", 3:"three"}
print(dic[2])
print(dic.get(5)) # print none if key not present

print(dic.keys())
print(dic.values())

for key in dic.keys():
    print(dic[key])
    print(f"the value of dic is {key} is {dic[key]}")

for key, value in dic.items():
    print("id : ",key, " value : ", value)


dic.update({4 :  "four"})
print(dic)

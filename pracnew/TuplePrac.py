# tuple used for crating unique values and values can not be changed
tup = (3,1,2,4,3,5,3,9,3)
print(type(tup))
print(tup)
print(tup[3:6])
res = tup.index(3,2,7)
print(res)
print(tup[3:6])

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)
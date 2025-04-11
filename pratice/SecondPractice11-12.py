# String chapter 11
st = "vikram"
print(st)
print(st[0]) # string is like an array of string
s = """C
vikram
v
 """
print(s)
for character in st:
    print(character)

fruit = "Mango"
print(fruit[0:4])
print(fruit[:len(fruit)])
# below both are equals
print(fruit[0:-3])
print(fruit[0:len(fruit) -3 ])


print(fruit[-3:-1]) # it means print(fruit[len(fruit) -3:len(fruit) -1 ])
print(fruit[len(fruit) -3:len(fruit) -1 ])



































print(fruit[-4:-2])

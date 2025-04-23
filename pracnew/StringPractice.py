# print("vikram")
# '''
# names = "this is a car"
# print(names[0])
# for character in names:
#     print(character)
# '''
# # String slicing
#
# fruit = "Mango"
# mangoLeng = len(fruit)
#
# print(mangoLeng)
# print(fruit[0:5]) # including 0 not 5
# print(fruit[1:4]) # including 1 not 4
# print(fruit[2:4])
# print(fruit[:5])
# # Below are same
# print(fruit[0:-3])
# print(fruit[0:len(fruit)-3])
# print(fruit[-1:len(fruit)-3]) # not possible as it will take [4,2]
# print(fruit[-3:-1])
#

# 13 day
#  string methods
a = "orange "
print(len(a))
print(a.upper())
print(a.lower())
print(a.strip())
b = "watermelon0!!!!!!!"
print(b.rstrip("!")) # only remove tailing character
print(a.replace("orange", "fruit"))

c = "capitalize the first characteR and small the otHers"
print(c.capitalize())
print(c.title()) # capital the all first character and small others
print(c.count("the"))

print(b.endswith("!!!"))

print(c.find("and")) # find the first occurrence of give string
print(c.find("andaa")) # find the first occurrence of give string if not find return -1
str1 = "welcome0"
print(str1.isalnum())
print(b.isalpha())

# ======================

# String formatting

letter = "hey my name is {} and i am from {}"
name = "Vikram"
country = "India"
# old approach
print(letter.format(name,country))
# new approach with string formatting
print(f"hey my name is {name} and I am from {country}")

price = 14.0148448
txt = f"for only {price:.2f} dollars"
print(txt)

# doc string

def square(n):
    '''takes in a number n, returns the square of n '''
    print(n**2)

square(5)
print(square.__doc__)
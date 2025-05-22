#import math
# from math import sqrt
# from math import *
import math as m
from vikram import welcome, vikram

# result = math.sqrt(9)
result = m.sqrt(9)
print(result)
welcome()
print(vikram)

x = 4

def myfunction():
    global x
    x = 5

print("print ", x)
def calculateGmean(a, b):
    mean = (a * b) / (a + b)
    print(mean)


def isGreater(a, b):
    if a > b:
        print("a is greater")
    else:
        print("b is greater")


a = 9
b = 8

calculateGmean(a, b)
isGreater(a, b)


# ===========================Function arguments
# default arguments
def average(a=9, b=1):
    print("average is : ", (a + b) / 2)


average()

# keyword argument -- order not require any order we can pass

average(b=10, a=2)

# Required arguments - mandatory arguments

average(a, b=5)


# keyword arbitrary arguments

def averageArbitrary(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("averageArbitrary is : ", sum / len(numbers))


averageArbitrary(8, 2, 1, 5)


# ==============================
# Dictionary
def name(**name):
    print("hello,", name["fname"], name["mname"], name["lname"])


name(fname="vikram", mname="kamboj", lname="vinayak")


def averageArbitrary(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum / len(numbers)

retvalue = averageArbitrary(4,5,6,7,8)
print("ret value : ", retvalue)
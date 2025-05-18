# a = int(input("Enter your age : "))
#
# if(a > 18):
#     print("your age is greater than 18")
# elif(a<18):
#     print("your age is less than 18")
# else:
#     print("your age is 18")

#==========================
#x is the variable to match
x =11
match x:
    case 0:
        print("x is zero")
    case 4 if x %2 == 0:
        print("x %2 ==0 and case is 4")
    case _ if x <10:
        print("x is <10")
    case _ :
        print(x)

#==============================
# for loop
name = "vikram"
for i in name:
    if(i=="k"):
        print("this is something special")

colors = ["red", "green", "blue", "black"]

for c in colors:
    print("color name : ", c)

for k in range(5):
    print(k+1)

for k in range(1,9):
    print("k 1-9 range : ", k )

for k in range(1,29,3):
    print("k range gap of 3 : ", k)


#=============================
# while loop

i =0;
while(i < 3):
    print(i)
    i = i+1

# break statement
for i in range(12):
    if(i==10):
        break
    print("5 x ", i +1, "= ", 5 * (i+1))

 # Continue statement
for i in range(12):
    if(i==10):
        continue
    print("5 x ", i +1, "= ", 5 * (i+1))


# for loop with else, else loop will only execute if for loop if full executed not it is break

for i in [1,2,3]:
    print(i)
else:
    print("sorry i not present")

# if it is break it will not execute else block
for i in [1,2,3]:
    print(i)
    if i==2:
        break
else:
    print("sorry i not present")

# =========================================
# Short hand if else

a = 330
b = 3303
print("A") if a>b else print("=") if a==b else print("B")

# ===================
# enumerates

index = 0
marks = [2,12,44,3,55,66]

for i in marks:
    print(i)
    if index ==3:
        print("wow")
    index +=1

for index, i in enumerate(marks):
    print(i)
    if index == 3:
        print("enumerates")

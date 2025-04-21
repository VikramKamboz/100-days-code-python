marks = [1,2,3,"harry", True, 5,7,9,11]
print(marks)
print(marks[:])
print(marks[1:-1])
print(marks[1:4])
print("print 1 : 8 first", marks[1:8])
print(marks[1:8:3])
for i in marks:
    print("all elements in list : " , i)

lstr = [i for i in range(4)]
print("create list : ", lstr)
lsttt = [i*i for i in range(10)]
print(lsttt)
lst = [i*i for i in range(10) if i%2==0]
print(lst)
a = input("Enter the number : ")
print(f"multiplication of number {a} is :")
try:
    for i in range(1, 11):
        print(f"{a} x {i} = {int(a) * i}")
except Exception as e:
    print(e)

print("print remaining code")
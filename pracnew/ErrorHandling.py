a = input("Enter the number : ")
print(f"multiplication of number {a} is :")
try:
    for i in range(1, 11):
        print(f"{a} x {i} = {int(a) * i}")
except Exception as e:
    print(e)

finally:
    print("execute finally block")

print("print remaining code")


# ========================

a = 4
if(a<5 or a>9):
    raise ValueError("value should be between 5 and 9")


x = int(input("Please enter a number: "))
y = int(input("Please enter a second number: "))
z = input("Please enter an operation: ")
if z == "*":
    print(x * y)
elif z == "-":
    print(x - y)
elif z == "+":
    print(x + y)
elif z == "/":
    print(x / y)
else:
    print("Please use an operation")
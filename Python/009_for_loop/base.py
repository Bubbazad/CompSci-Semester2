x = int(input("Please enter a line length "))
y = (input("Please enter V for Vertical or H for Horizontal "))
if y == "V":
    for z in range(0,x):
        print(".")
if y == "H":
    for z in range(0,x):
        print(".", end=" ")
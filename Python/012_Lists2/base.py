import random
List = []
x = int(input("How many Numbers do you want to generate? "))
for i in range(0,x):
    List.append(random.randrange(1,11))
for i in range(0,x):
    print(List[i], end = ", ")
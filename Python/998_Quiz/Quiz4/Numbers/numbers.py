mynumbers = [6,9,32,28,15,22,3,18]
x = 0
for i in range(len(mynumbers)):
    for y in range(len(mynumbers)):
        if mynumbers[i] >= mynumbers[x]:
            x = x + 1
        else:
            y = len(mynumbers)
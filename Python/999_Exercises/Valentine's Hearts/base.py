# import datetime
import random
People = []
Compliment = []
with open('People.txt') as f:
    for line in f:
        l = line.strip()
        People.append(l)
        
with open('Compliment.txt') as f:
    for line in f:
        l = line.strip()
        Compliment.append(l)
f.close()

input("Do you want a compliment? ")
C = random.randrange(26)
P = random.randrange(26)
print(People[P] + " " + Compliment[C])

# x = datetime.datetime.now()
# print()
# print("The date and time are:")
# print(str(x.day) + "/" + str(x.month) + "/" + str(x.year) + " at " + str(x.hour))
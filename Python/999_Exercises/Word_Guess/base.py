import random
List = []
with open('wordle.txt') as f:
    for line in f:
        i = line.strip()
        List.append(i)
f.close()
x = random.randrange(2315)
Wordle = List[x]
print("Guess a 5 letter word!")
for z in range(0,10):
    Guess = input()
    if Guess == Wordle:
        print("Good Job!")
    else:
        print("Bad Job!")
print(Wordle)
Guess = input()
if Guess == Wordle:     
    print("Good Job!")
else:
    print("Bad Job!")

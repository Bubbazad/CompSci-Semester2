import random
Resturants = ["Arbys", "Burger King", "Carls Jr"]
Arbys = ["Buffalo Roast","Smokehouse Brisket","Corned Beef Rubeun"]
Burger_King = ["Whopper","Hamburger","Cheeseburger"]
Wendys = ["Baconator","Jr. Cheesebruger","Big Bacon Cheddar Triple"]
R = input("Where do you want to eat? Wendys, Burger King, or Arbys?")
if R == "Arbys":
    print(Arbys)
    print(random.choice(Arbys))
if R == "Wendys":
    print(Wendys)
    print(random.choice(Wendys))
if R == "Burger King":
    print(Burger_King)
    print(random.choice(Burger_King))
FoodList = []
PriceList = []
x = int(input("How many items do you want to buy? "))
Total = 0
for z in range(0,x):
    FoodList.append(input("What item are you purchasing? "))
    PriceList.append(float(input("How much was the item? ")))
    print("-----------------------------------------------")
print("                   Your Receit")
print("-----------------------------------------------")
for i in range(0,x):
    print(FoodList[i] + " -", end = " ")
    print("$", end = "")
    print(PriceList[i])
    Total = Total + PriceList[i]
print("Your total is " + str(Total))
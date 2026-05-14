foods = []
prices = []
total = 0

while True:
    food = input("enter the food name or q to quit : ")
    if food.lower() == "q":
        break
    else :
        price = float(input(f"enter the price of a {food} : "))
        foods.append(food)
        prices.append(price)
        
print("-------Your kart------")
for food in foods:
    print(food , end =" ")
    
for price in prices:
    total += price

print(f"Your total is : ${total}")



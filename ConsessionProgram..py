menu = {
    "idly": 50,
    "dosa": 100,
    "sambarVada": 60,
    "pongal": 70,
    "coffee": 10,
    "tea": 10,
    "juice": 20,
    "water": 10,
    "snacks": 20,
    "dessert": 20}

cart  = []
total = 0

print("--------------------------")
for key , value in menu.items():
    print(f"{key:10} : ${value}")
print("--------------------------")
    
while True:
    food = input("Enter what you want to order (q to exit):").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        
print(cart)
     
for food in cart:
    total += menu.get(food)
    print(food , end=" ")

print()
print(f"Total amount is: ${total}")


    
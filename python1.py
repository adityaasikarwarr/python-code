# format specifiers = {value : flags } format a value based on what flags are inserted
# :f for floating point numbers
# :.nf for n floating point numbers
# :n for integers
# :<n for left alignment
# :>n for right alignment
# :^n for center alignment
# :+n for sign
# :n for padding
# price1 = 5000
# price2 = 23.865346
# price3 = 4000
# print(f"the price 1 is {price1 : .2f} dollars")
# print(f"the price 2 is {price2 : .2f} dollars")
# print(f"the price 3 is {price3 : .2f} dollars")



# name = input("enter your namme")
# while name == "":
#     print("you did not enter your name")
#     name = input("enter your namme")
# print(f"hello {name}")

# food = input("Enter a food you like and  press q to exit")
# while not food == "q":
#     print(f"you like {food}")
#     food = input("Enter a food you like and  press q to exit")
# print("bye")


num = int(input("enter a number 1 and 10 "))
while num < 1 or num > 10:
    print(f"your {num} is not valif")
    num = int(input("enter a number 1 and 10 "))
print("thank you")
operator = input("Enter the operator (+, -, *, /): ")
num1 = float(input("Enter the first number: "))
num2  = float(input("Enter the second number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("invalid operator")

age = int(input("Enter a number: "))

if age >= 18:
    print("you are eligible for voting")
else:
 print("you are not eligible for voting")
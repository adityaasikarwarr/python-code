hello = lambda x : print("Hello, " + x + "!")
hello("Alice")


var = lambda : print("This is a lambda function with no arguments.")
var()


add = lambda x, y : x + y
print(add(5, 3))


n = int(input("Enter a number: "))
check = lambda n : "even" if n % 2 == 0 else "odd"
print(check(n))


year = int(input("Enter your year : "))
leapyear = lambda year : print("leap year") if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)) else print("not leap year")
leapyear(year)


num1 = int(input("Enter your number 1 : "))
num2 = int(input("Enter your number 1 : "))
num3 = int(input("Enter your number 1 : "))
largest1 = lambda num1 , num2 : print("num1 is greatest") if num1 > num2 else print("num2 is greater")
largest1 = lambda num1 , num2 , num3 : num1 if num1 > num2 and num1 > num3 else (num2 if num2 > num1 else num3)
largest2 = lambda num1 , num2 , num3 : max(num1 , num2 , num3)
largest1(num1 , num2)
print(largest2(num1 , num2 , num3))


string = input("Enter your word : ")
palindrome = lambda string : print(string[::-1])
palindrome2 = lambda string : print("palindrome") if str(string) == str(string[::-1]) else print("not a palindrome")
palindrome(string)
palindrome2(string)
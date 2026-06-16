hello = lambda x : print("Hello, " + x + "!")
hello("Alice")

var = lambda : print("This is a lambda function with no arguments.")
var()

add = lambda x, y : x + y
print(add(5, 3))

n = int(input("Enter a number: "))
check = lambda n : "even" if n % 2 == 0 else "odd"
print(check(n))
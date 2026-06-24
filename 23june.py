
# Given a list of employee salaries, use filter() to select salaries greater than ₹50,000 and map() to add a 10% bonus.

salaries = [60000, 45000, 75000, 55000, 80000, 40000, 90000]
filtered = filter(lambda x : x > 50000 , salaries)
bonus = list(map(lambda x : x * 1.10 , filtered))

print(bonus)

# Given a list of integers, use filter() to select even numbers and map() to calculate their cubes.

nums = [ 12 ,45 ,233,64,6,69,28, 47]
select = filter(lambda x : x % 2 == 0 , nums)
cubes = list(map(lambda x : x ** 3 , select))
print(cubes)

# Given a list of student marks, use filter() to select marks greater than or equal to 40 and map() to add 5 grace marks.

marks = [ 45,99,45,87,98,85,54, 84 , 40 , 44 , 33]
select = filter(lambda x : x >= 40 , marks)
add = list(map(lambda x : x + 5 , select))
print(add)

# Given a list of strings, use filter() to select strings whose length is greater than 5 and map() to convert them to uppercase.

strings = [ "hello", "nice", "millionaire", "billionaire" , "trillionaire" ]
select = filter(lambda x : len(x) > 5 , strings)
convert = list(map(lambda x : x.upper() , select ))
print(convert)

# Given a list of years, use filter() to select leap years and map() to convert them into strings.

years = [1000 , 2000 , 2004 , 2012 , 2016 , 2020 , 2024 , 2026]
select = filter(lambda x: (x % 400 == 0) or (x % 4 == 0 and x % 100 != 0),years)
convert = list(map(lambda x : str(x) , select))
print(convert)

# modules in python are files that contain python code and can be imported into other python files. they can contain functions, classes, and variables. they can also include runnable code. modules are a way to organize code into manageable sections. they can be built-in or user-defined.

# math module is a built-in module in python that provides mathematical functions. it includes functions for trigonometry, logarithms, exponentials, and more. to use the math module, you need to import it using the import statement. once imported, you can access the functions and constants defined in the math module.

# random module is a built-in module in python that provides functions for generating random numbers. it includes functions for generating random integers, floating-point numbers, and sequences. to use the random module, you need to import it using the import statement. once imported, you can access the functions defined in the random module.

# randint() function is a function in the random module that generates a random integer between two specified values. it takes two arguments, the lower and upper bounds, and returns a random integer within that range. for example, random.randint(1, 10) will return a random integer between 1 and 10, inclusive.

# randrange() function is a function in the random module that generates a random integer within a specified range. it takes three arguments: start, stop, and step. it returns a random integer from the range defined by these arguments. for example, random.randrange(1, 10, 2) will return a random odd integer between 1 and 9.

# choice() function is a function in the random module that selects a random element from a non-empty sequence. it takes a single argument, which is the sequence (like a list or tuple), and returns a randomly selected element from that sequence. for example, random.choice(['apple', 'banana', 'cherry']) will return one of the fruits randomly.

# shuffle() function is a function in the random module that randomly shuffles the elements of a list in place. it takes a single argument, which is the list to be shuffled, and modifies the list directly. for example, if you have a list my_list = [1, 2, 3, 4], calling random.shuffle(my_list) will rearrange the elements of my_list in a random order.
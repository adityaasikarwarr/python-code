
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
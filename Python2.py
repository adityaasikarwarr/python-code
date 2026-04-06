# fact = 1
# n = 5
# while n != 0:
#      fact = fact * n
#      n = n - 1
# print(fact)

# i = 1
# while i <= 50:
#      if i % i == i:
#       print(i)

# def addition(*args):
#     print(type(args))
#     a, b, c, d = args
#     print(a, b, c, d)
   
# addition(10 , 20 , 30 , 40)

# def add(a , b,c ,d,e,f,g,h):
#     print(a + b + c + d + e + f + g + h)

# add(12,667,323,13,6,8,9,99)

# def info(name , section , course):
#     print("name : " + name)
#     print("section : " + section)
#     print("course : " + course)
# info(name = "Aditya" , section = "A" , course = "B.tech")

def infos(**details):
    print(details)
    print(type(details))
infos(name = "Aditya" , section = "A" , course = "B.tech" , building = "A")

def academic(**details):
    print(details)
    for i , j in details.items():
        print(i , j)
academic(name = "Aditya" , section = "A" , course = "B.tech" , building = "A")
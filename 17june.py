l = [x for x in range(1, 11)]
print(l)

even = [x for x in range(1, 11) if x % 2 == 0]
print(even)

even1 = ["even" if x % 2 == 0 else "odd" for x in range(1 , 11)]
print(even1)

print({x for x in range(1 , 11)})

print({x for x in range(1 , 11) if x % 2 == 0})

print({"even" if x % 2 == 0 else "odd" for x in range(1, 11)})

string = eval(input("enter your list of string : "))
findOut = [x for x in string if type(x) == str and x == x[::-1]]
print(findOut)

check = [x ** 2 if x % 2 == 0 else x ** 3 for x in range(1,11)]
print(check)


class hey :
    
    def sum(self):
        print("hello")
        
    def sum(self , a , b):
        return a + b
    
    def sum(self , a , b , c):
        return a + b + c
    
obj = hey()
obj.sum()
print(obj.sum(2 , 3))
print(obj.sum(2 , 3 , 4))
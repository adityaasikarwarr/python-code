l = [x for x in range(1, 11)]
print(l)

even = [x for x in range(1, 11) if x % 2 == 0]
print(even)

even1 = ["even" if x % 2 == 0 else "odd" for x in range(1 , 11)]
print(even1)
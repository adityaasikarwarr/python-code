t = (1,2,3,4,5,7,8,9,10)
print(t[3])
print(t[-4])

for i in t:
    if i == 4:
        print("yes exists")
    
print(11 in t)

a = [(1,"a"), (3,"b"), (5,"c")]
val = zip(*a)
print(list(val))

newA = []
for  x , y in a:
    newA.append((x, 0))
print(newA)

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
    newA.append((x, 100))
print(newA)

s = "Python"
print(s[0])
print(s[5])
print(s[-4])

numbers = [10 , 20 , 30 , 40 , 50]
print(numbers[0])
print(numbers[-1])
print(numbers[-2])

word = "Programming"
print(word[3])
print(word[-7])
print(word[2])

s = "PythonProgramming"
print(s[0:6])
print(s[6:17])

numbers = [10,20,30,40,50,60,70]
print(numbers[1:4])
print(numbers[4:7])

text = "ABCDEFGHIJ"
print(text[0:9:2])
print(text[1:9:2])

student = {"name":"Rahul","age":20,"marks":75}
student["marks"] = 85
print(student)
    
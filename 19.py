a = open('19.txt', 'r')
print(a.read().split("\n"))
a.close()

b = open('19.txt', 'a')
b.write("\nThis is the new line added to the file.")
b.close()

c = open('19.txt', 'r')
print(c.read().split("\n"))
c.close()
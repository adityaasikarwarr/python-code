principle = 0
rate = 0
time= 0

while principle <= 0:
    principle = float(input("enter the principle amount :"))
    if principle <= 0:
        print("principle must be greater than 0")
        
while rate <= 0:
    rate = float(input("enter the rate :"))
    if rate <= 0:
        print("rate must be greater than 0")
        
while time <= 0:
    time = float(input("enter the time in years :"))
    if time <= 0:
        print("time must be greater than 0")
total= principle* pow((1+rate/100), time)
print(f"your total amount is :\t{total}")
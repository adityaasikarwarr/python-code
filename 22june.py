# Create a Vehicle Insurance System. Create a Vehicle class and a child class InsurancePolicy. Store premium amount as a private variable and create methods to pay premium and display policy details.

class Insurance :
    
    def __init__(self , carNumber , carBrand ):
        self.carNumber = carNumber
        self.carBrand = carBrand
        self.__premium = 0
        
    def get_premium(self):
        return self.__premium
    
    def add_premium(self , amount):
        self.__premium += amount

class Policy(Insurance) :
    
    def __init__(self, carNumber, carBrand):
        super().__init__(carNumber, carBrand)
        
    def pay_premium(self):
        pay = int(input("Enter amount to be paid : "))
        self.add_premium(pay)
        print(f"Premium of ₹{pay} paid successfully")
        
    def show_details(self):
        print("CAR INSURANCE DETAILS")
        print(f"Car number = {self.carNumber}")
        print(f"Car Brand = {self.carBrand}")
        print(f"Premium Paid = {self.get_premium()}")
        
obj = Policy(5678 , "DEFENDOR")
obj.pay_premium()
obj.show_details()

# Create a Movie Streaming Subscription System. Create a User class and a PremiumUser class. Store subscription amount privately and create methods to renew the subscription and display account details.

class User :
    def __init__(self , userName , UserId ):
        self.Name = userName
        self.userId = UserId
        self.__amount = 0
        
    def pay(self):
        return self.__amount
    
    def add_amount(self , amount):
        self.__amount += amount
        
    def renew(self):
        
        new = input("Want to renew or not (yes or no ) :").lower()
        
        if new == "yes":
            amount = int(input("Enter your subs amount : "))
            self.add_amount(amount)
            print("Your subscription has been restored")
            
        else :
            print("Subscription Cancel")
        
    def show_details(self):
        print("CUSTOMER DETAILS")
        print(f"Customer Name = {self.Name}")
        print(f"Customer ID = {self.userId}")
        print(f"Subscription Amount = {self.pay()}")
        
        
class PremiumUser(User):
    def __init__(self, userName, UserId , premiumUser):
        super().__init__(userName, UserId)
        self.premiumUser = premiumUser

obj = PremiumUser("Ramesh", 100 , "Unlimited Downloads")
obj.renew()
obj.show_details()
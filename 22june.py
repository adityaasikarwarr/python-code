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
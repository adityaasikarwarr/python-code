# Create a Library Membership System. Store member details using a constructor. Use inheritance to create PremiumMember. Keep membership fee private. Create methods to issue books, return books, and display details

class Member :
    def __init__(self, customName, CustomAge , customFee):
        self.Name = customName
        self.age = CustomAge
        self.__MembershipFee__ = customFee
        self.book_issued = []
        
    def issue_books(self):
        self.book_name = input("ENTER BOOK YOU WANTED TO ISSUE :")
        self.book_issued.append(self.book_name)
        print(f"book issued to : {self.Name}")
        
    def return_books(self):
        
        self.return_book = input("Enter book name to return : ")
                 
        if self.return_book in self.book_issued:
            self.book_issued.remove(self.return_book)
            print(f"Book returned by : {self.Name}")
        else :
            print("No books to return")
            
    def get_fee(self):
        return self.__MembershipFee__
            
    def display_details(self):
        print("CUSTomer Details")
        print(f"Customer Name : {self.Name}")
        print(f"Customer age : {self.age}")
        print(f"Customer Fee : {self.__MembershipFee__}")
        print(f"Book issued : {self.book_issued}")
        
class premium(Member):
    
    def __init__(self, customName, CustomAge, customFee , PremiumBenefits):
        super().__init__(customName, CustomAge, customFee)
        self.benefits = PremiumBenefits
        
    def display_details(self):
        super().display_details()
        print(f"Premium Benefits : {self.benefits}")
     
member = premium("Ramesh" , 20 , 2000 , "Unlimited books can be issued")
member.issue_books()
member.return_books()
member.display_details()
    
    
# Create a Restaurant Ordering System. Store customer details using a constructor. Create a child class Order that stores order details. Use encapsulation for the bill amount and create methods to add items and generate the bill.

class OrderingSystem :
    
    def __init__(self , Name , contact  ,  billNumber):
        self.Name = Name
        self.contact = contact
        self.Bill_Number = billNumber
        self.__total = 0
        self.items = []
        
    def get_bill(self):
        return self.__total
        
class Order(OrderingSystem):
    def __init__(self, Name, contact, billNumber ,):
        super().__init__(Name, contact, billNumber)
        
    def add_items(self):
        item = input("Enter the food item you want order : ")
        price = int(input('Enter the price of item : '))
        self.price = price
        
        self.items.append(item)
        self._OrderingSystem__total += price
        print(f"your item {item} amount {price} has been added")
    
        
    def show_details(self):
       print("\nCUSTOMER DETAILS")
       print("Customer Name :", self.Name)
       print("Customer Contact :", self.contact)
       print("Bill Number :", self.Bill_Number)
       print("Items :", ", ".join(self.items))
       print("Total Bill :", self.get_bill())
        
obj = Order("Rajesh", 999999999 , 991)
obj.add_items()
obj.add_items()

obj.show_details()
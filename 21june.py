# Create a Library Membership System. Store member details using a constructor. Use inheritance to create PremiumMember. Keep membership fee private. Create methods to issue books, return books, and display details

class Member :
    def __init__(self, customName, CustomAge , customFee):
        self.Name = customName
        self.age = CustomAge
        self.__MembershipFee__ = customFee
        self.book_issued = []
        
    def issue_books(self):
        self.book_name = input("ENTER BOOK YOU WANTED TO ISSUE :")
        self.book_issued.append(self.book_issued)
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
    

class A :
    __A = 10
    _B = 20
    
    def _disp(cls):
        print(cls.__A)
        print(cls._B)
        
obj = A()
obj._disp()

class B:
    def getter(cls):
        print(cls._A)
    def setter(cls, value):
        cls._A = value
        
        
class student :
    __marks = 0
    
    def marks(self , marks):
        self.__marks = marks
    def disp(self):
        print(self.__marks)
        
obj = student()
obj.marks(85)
obj.disp()


class BankAcc :
    __balance = 0
    
    def addMoney(self):
        self.amount = int(input("Enter the amount : "))
        
        if self.amount > 0 :
            self.__balance += self.amount
            print("valid amount added")
        else :
            print("Invalid amount") 
            
    def withdraw(self):
        self.withdraw = int(input("Enter the amount to withdraw : "))
        if self.withdraw <= 0 :
            print("Invalid amount entered")
        elif self.withdraw > self.__balance :
            print("Insufficient balance ")
        else :
            self.__balance = self.__balance - self.withdraw
            print("Amount withdrawn : " , self.withdraw)
            
    def disp(self):
        print("Amount left in account : " , self.__balance)
        
obj = BankAcc()
obj.addMoney()
obj.withdraw()
obj.disp()
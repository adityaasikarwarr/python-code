from abc import ABC,abstractmethod

class BankApp(ABC) :
    
    def database(self):
        print('connected to database')
        
    @abstractmethod
    def security(self):
        pass
   
class MobileApp(BankApp):
    
    def login(self) :
        print("login success")
        
    def security(self):
        print("mobile app security")
        
app = MobileApp()
app.database()
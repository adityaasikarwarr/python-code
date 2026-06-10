class Animal :
    def eat(self):
        print("eat")
        
class Dog(Animal):
    def bark(self):
        print("bark")
        
Dogobj = Dog()
Dogobj.eat()
Dogobj.bark()


class Employee :
    employee_name = "harsh raj"
    employee_salary = 100000
     
class Developer(Employee):
    programming_language = "Java , Python "
    
employeedetails = Developer()
print(employeedetails.employee_name)
print(employeedetails.employee_salary)
print(employeedetails.programming_language)


class Resume10 :
    
    def __init__(self):
        self.name = input("Enter your name : ")
        self.roll = int(input("Enter your roll : "))
        self.section = input("enter your section : ")
        self.section_class = int(input("enter your class : "))
        self.marks = int(input("enter your marks :"))
        
    def display_10th(self):
        print("10th name = ", self.name)
        print("roll = ", self.roll)
        print("section = ", self.section)
        print("Class = ", self.section_class)
        print("marks = ", self.marks)
        
    
class Resume12th(Resume10):
    
    def __init__(self):
        super().__init__()
    
        self.marks_12th = int(input("Enter your 12th marks"))
        
    def display_12th(self):
        self.display_10th()
        print("12th Marks = ", self.marks_12th)
    
class ResumeDegree(Resume12th):
    def __init__(self):
        super().__init__()
        
    def display_resume(self):
        self.degree_name = input("Enter your degree name : ")
        self.degre_year = int(input("Enter your degree completion year : "))
        self.degree_status = input("enter your degree status : ")
        self.display_12th()
        print("Degree name = ", self.degree_name)
        print("Degree completion year = ", self.degre_year)
        print("Degree status = ", self.degree_status)

student1 = ResumeDegree()
student1.display_resume()

class Bank:
    bank_name = "HDFC"
    bank_address = "Mohali"
    
    def info(self,name, age , account_number,acc_balance):
        self.name = name
        self.age = age
        self.account_number = account_number
        self.acc_balance = acc_balance
        
    def display(self):
        print("Name = ", self.name)
        print("Age = ", self.age)
        print("Account number = ", self.account_number)
        print("Account balance = ", self.acc_balance)
        
    def deposit(self, value):
        self.acc_balance = self.acc_balance + value
        print("value added ", value)
        
    def withdraw(self, w_bal):
        self.acc_balance = self.acc_balance - w_bal
        print("Withdraw", w_bal)
        
ob = Bank()
ob.info("Ajit", 20, 126262662,2000)
ob.display()
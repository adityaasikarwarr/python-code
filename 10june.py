# class Animal :
#     def eat(self):
#         print("eat")
        
# class Dog(Animal):
#     def bark(self):
#         print("bark")
        
# Dogobj = Dog()
# Dogobj.eat()
# Dogobj.bark()


class Employee :
    employee_name = "harsh raj"
    employee_salary = 100000
     
class Developer(Employee):
    programming_language = "Java , Python "
    
employeedetails = Developer()
print(employeedetails.employee_name)
print(employeedetails.employee_salary)
print(employeedetails.programming_language)


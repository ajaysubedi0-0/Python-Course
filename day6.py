# # # # #_-_-_-_-_-_-_-_-_-Encapsulation_-_-_-_-_-_-_-_-_-_-_-_-_-_#


# # # # class BankAccount:
# # # #     def __init__(self,account_number,balance):
# # # #         self._account_number = account_number
# # # #         self.balance = balance
# # # #     def depsit(self,amount):
# # # #         self.balance += amount
# # # #         print(f'deposit sucessful. New Balance : ${self.balance}')
# # # #     def checkbalance(self):
# # # #         print(f'current balance : {self.balance}')
# # # #     def withdraw(self,amount):
# # # #         self.balance -= amount
# # # #         print(f'Withdraw sucessful. New balance: ${self.balance}')
# # # # account = BankAccount('1234',1000)
# # # # account.checkbalance()
# # # # account.withdraw(300)
# # # # print(account._account_number)
# # # # # account.depsit(2000)

# # # class Employee:
# # #     def __init__(self,name,emp_id,salary):
# # #         self._name = name
# # #         self._emp_id =emp_id
# # #         self.__salary = salary

# # #     def calc_bonus(self):
# # #         return self.__salary * 0.1 + self.__salary

# # #     def display_info(self):
# # #         print(f'Name : ${self._name}')
# # #         print(f'Employee ID : ${self._emp_id}')
# # #         print(f'Salary : ${self.__salary}')

# # # employee = Employee('Bob',1024,7000)
# # # # employee._name
# # # employee.display_info()
# # # bonus = employee.calc_bonus()
# # # print(bonus)





# # #-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-Abstraction-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#

# # class Rectangle:
# #     def __init__(self,length,width):
# #         self.length = length
# #         self.width = width

# #     def calculate_perimeter(self):
# #         return 2*(self.length + self.width)
# #     def get_perimeter(self):
# #         return 2*(self.length + self.width)
# # rectangle = Rectangle(1,3)
# # perimeter = rectangle.get_perimeter()
# # print(perimeter)

# #-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-Inheratance-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#


# class Vehicle:
#     def __init__(self,name,model,year,color):
#         self.name = name
#         self.model = model
#         self.year = year
#         self.color = color
#     def display_info(self):
#         print(f'Name : {self.name}')
#         print(f'model : {self.model}')
#         print(f'year : {self.year}')
#         print(f'color : {self.color}')


# class Car(Vehicle):
#     def __init__(self, name, model, year, color, num_doors):
#         super().__init__(name,model, year,color)
#         self.num_doors = num_doors

#     def display_info(self):
#         super().display_info()
#         print(f'NUmber of doors : {self.num_doors}')

# class Bike(Vehicle):
#     def __init__(self, name, model, year, color, engine_size):
#         super().__init__(name, model, year, color)
#         self.engine_size = engine_size
    
#     def display_info(self):
#          super().display_info()
#          print(f'The engine size is : {self.engine_size}')

# car = Car('Hundai','Creta SX(O)',2020,'white',4)
# car.display_info()
    






class Employee:
    def __init__(self,name,emp_id):
        self.name = name
        self.emp_id = emp_id
    
    def display_info(self):
        print(f'Name : {self.name}')
        print(f'Employee ID : {self.emp_id}')
        

class Manager(Employee):
    def __init__(self, name, emp_id,Dep_id):
        super().__init__(name, emp_id)
        self.department = Dep_id
    def display_info(self):
        super().display_info()
        print(f'Department ID : {self.department}')

class Progammer(Employee):
    def __init__(self, name, emp_id, Lan, post):
        super().__init__(name, emp_id)
        self.Lan = Lan
        self.post = post
    def display_info(self):
         super().display_info()
         print(f'Progamming language : {self.Lan}')
         print(f'Post : {self.post}')

manager = Manager('Bob',12058,5)
progammer = Progammer('bobie',12059,'c++','Software Engineer')
manager.display_info()
progammer.display_info()
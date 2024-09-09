#-_-_-_-_-_-_-_-_-_-_-_-_-_-_- OOP _-_ Based - _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#

class Calculation:
    def add(self,a,b):
        return a+b
    
calculator =Calculation()
result2 = calculator.add(1,2)
print(result2)



#_-_-_-_-_-_-_-_-_-_-_-_-_-_-Inheritance_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#


# class animal:
#     def __init__(self,name): #(__init__) is a constructor
#         self.name = name
    
#     def eat(self):
#         print('I can eat')

#     def sleep(self):
#         print('I can sleep')

# class Dog:
#     def __init__(self,name): #(__init__) is a constructor
#         self.name = name
    
#     def eat(self):
#         print('I can eat')

#     def sleep(self):
#         print('I can sleep')




class Animal:
    def __init__(self,Name):
        self.Name = Name
    def eat(self):
        print('I can eat')
    def sleep(self):
        print('I can sleep')


class Dog(Animal):
    def bark(self):
        print('I can bark')


dog1 = Dog('german shepared')
# dog1.eat()

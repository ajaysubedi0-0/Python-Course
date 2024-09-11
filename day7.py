# # #-_-_-_-_-_-_-_-_-_-_-Polymorphism-_-_-_-_-__-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
 
# # #--------Method-Overiding---------------#
# # class Shape:
# #     def area(self):
# #         pass 

# # class Circle(Shape):
# #     def __init__(self,radius):
# #         self.radius = radius
    
# #     def area(self):
# #         return 3.14 * self.radius ** 2
    
# # class Rectangle(Shape):
# #     def __init__(self,length,width):
# #         self.length = length
# #         self.width = width

# #     def area(self):
# #         return self.length * self.width
    
# # def print_area(shape):
# #     print('area :',shape.area())
    
# # rectangle = Rectangle(5,2)
# # circle = Circle(12)
# # #--Method 1--#
# # print_area(rectangle)
# # print_area(circle)
# # #--Method 2--#
# # shapes = [Rectangle(5,2),Circle(4)]
# # for shape in shapes:
# #     print_area(shape)



# class Animal:
#     def speak(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         return 'Bark'
    
# class Cat(Animal):
#     def speak(self):
#         return 'meew'
    
# def sound(animal):
#     print(animal.speak())


# animals = [Dog(),Cat()]
# for animal in animals:
#     sound(animal)\


class Employee:
    def __init__(self,name):
        self.name = name
    def calc_salary(self):
        pass

class FullTimeEmployee(Employee):
    def calc_salary(self):
        return 50000

class partTimeEmployee(Employee):
    def calc_salary(self):
        return 20000
    
employees = [FullTimeEmployee('Bob'),partTimeEmployee('Oggy')]
for employee in employees:
    print(f"{employee.name}'s salary",employee.calc_salary())
#------------------ Basic Loop ----------------#

# x = 0

# # if x>0:
# #     print("x is positive")
# # elif x<0:
# #     print('x is negative')
# # elif x == 0 :
# #     print('x is zero')
# x =10
# y=-10
# z = 0
# if x>0 and y>0:
#     print('both are positive')
# elif x<0 and y<0:
#     print('both are negative')
# elif x<0 and y>0:
#     print('x is Negative and y is positive')
# elif x>0 and y<0: 
#     print('x is positive and y is negative')







#-------------------------- Loop of fruits -------------------#

# fruits= ['apple','banana','mango']

# for fruit in fruits:
#     print(fruit)








#---------- Student Score Loop --------------#

# print(student_grades.items())

# for student in student_grades:
#                      print(student,'scored',student_grades[student])


###################################################################################
# for student,grade in student_grades.items():
#     print(student,'scored',grade)



#---------------------


student_grades = {
    'pranjal' : 90,
    'gopu' :49,
    'mandip' : 78
}
for value in student_grades.values():
    print(value)

# message = 'This much for today!'
# for loop in message:
#     print(loop)





for num in range(1,11):
    print(num)
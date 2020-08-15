# class Teddy:
#     quantity = 200
#
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#     def change_color(self, color):
#         self.color = self


# Teddy1 = Teddy('Harry', 'White')
# print(Teddy1.name)
# print(Teddy1.color)
#
#
# (Teddy1.change_color('Red'))
# print(Teddy1.name)
# print(Teddy1.color)
# Teddy2 = Teddy('Tammy', 'Brown')
# print(Teddy2.name)
# print(Teddy2.color)

# class Student:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def student_records(self, name, age):
#         self.name = name
#         self.age = age
#         # print(self.name)
#         # print(self.age)
#
#
# student1 = Student("", "")
# name = input("Enter your name ")
# age = input("Enter your age  ")
# student1.student_records(name, age)
#
#
# class Science_student(Student):
#
#     def science(self, name, age):
#         print('This is a science object')
#
#
# ss = Science_student("", "")
# ss.student_records(name, age)

# MULTIPLE INHERITANCE:

# class A:
#     def a_method(self):
#         print('this is method A')
#
#
# class B:
#     def b_method(self):
#         print('this is method B')
#
#
# class C(A, B):
#     def c_method(self):
#         print('this is method c')
#
#
# c_object = C()
# c_object.a_method()
# c_object.b_method()
# c_object.c_method()

# MULTILEVEL INHERITANCE
# class A:
#     def a_method(self):
#         print('this is method A')
#
#
# class B(A):
#     def b_method(self):
#         print('this is method B')
#
#
# class C(B):
#     def c_method(self):
#         print('this is method c')


# c_object = C()
# c_object.a_method()
# c_object.b_method()
# c_object.c_method()

# RECURSION IN PYTHON

# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return x * factorial(x-1)
#
#
# print(factorial(1))

# numbers = {2,2,5,5,7,89}
# print(numbers)
# print(89 in numbers)


# from itertools import count
#
# for i in count(3):
#     if i>=20:
#         break
#     print(i)


# from itertools import accumulate, takewhile
#
# numbers = list(accumulate(range(11)))
# print(numbers)
# print(list(takewhile(lambda x: x <=10, numbers)))

# class Point():
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return x, y
#
# point1 = Point(4, 5)
# point2 = Point(3,6)
# location = point1 + point2
# print(location)


# class My_class:
#     __hidden_variable = 0
#
#     def add(self, increment):
#         self.__hidden_variable += increment
#         print(self.__hidden_variable)
#
#
# object1 = My_class()
# object1.add(6)

# class Computer:
#
#     def __init__(self, RAM, memory, processor):
#         self.RAM = RAM
#         self.memory = memory
#         self.processor = processor
#
#     def get_specs(self):
#         print('Enter the details')
#         self.RAM = input('Enter the RAM size ')
#         self.memory = input('memory size ')
#         self.processor = input('Enter processor ')
#
#     def print_specs(self):
#         print('The RAM size is {}, memory is {} and processor is {} '.format(self.RAM,self.memory,self.processor))
#
#
# class Desktop(Computer):
#
#     def __init__(self, casecolor):
#         self.casecolor = self
#
#     def get_case_details(self):
#         self.casecolor = input('Enter the color of your system ')
#
#     def print_desk_specs(self):
#         print('the casecolor is {}'.format(self.casecolor))
#
#
# desktop1 = Desktop("")
# desktop1.get_specs()
# desktop1.print_specs()
# desktop1.get_case_details()
# desktop1.print_desk_specs()


# class Number:
#
#     def __init__(self, x):
#         self.x = x
#
#     def __mul__(self, other):
#         x = self.x + other.x
#         return x
#
# number1 = Number(5)
# number2 = Number(6)
# print(number1 * number2)


# import re
# pattern = r"@gmail"
#
# if re.match(pattern, "harshitpadaliya5@gmail.com"):
#     print('Match Found')
# else:
#     print('No match found')
#
# if re.search(pattern, "harshitpadaliya5@gmail.com"):
#     print('Match Found')
# else:
#     print('No match found')
#
#
# print(re.findall(pattern, "harshitpadaliya5@gmail.com"))

# string = "hi my name is harry and harry is 30 years old"
# pattern = r"harry"
# new_string = re.sub(pattern, "harshit", string)
# print(new_string)

# import re
# pattern = r"gr..n"
# if re.match(pattern, "green"):
#     print('Match Found')

# import re
# pattern = r"^udemy.com$"
# if re.search(pattern,'udemy.com'):
#     print


# import re
#
# pattern = r"[A-Z][a-z][0-9]"
# if re.search(pattern, 'Aa9'):
#     print("match found")

# import re
# pattern1 = r"harry(bacon)*"
# pattern2 = r"bread(eggs)*bread"
#
# if re.match(pattern2, 'breadeggsbread'):
#     print('M Found')
#
# from tkinter import *
#
# root = Tk()
#
# label1 = Label(root, text="Hi this is a demo window")
# label1.pack()
#
# root.mainloop()


# frame1 = Frame(root)
# frame1.pack()
#
# frame2 = Frame(root)
# frame2.pack(side=BOTTOM)
#
# button1 = Button(frame1, text="Click here", fg ='Red')
# button1.pack()
#
# button2 = Button(frame2, text="navigate", fg='Blue')
# button2.pack()

label1 = Label(root, text="FirstName")
label2 = Label(root, text="LastName")

entry1 = Entry(root)
entry2 = Entry(root)

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)


label1 = Label(root, text="First", bg="Red", fg="White")
label1.pack(fill=X)

label2 = Label(root, text="Last", bg="Blue", fg="White")
label2.pack(side=LEFT, fill=Y)

def dosomething():
    print('Welcome to the website')


button1 = Button(root, text='Enter Address', command=dosomething, fg="White", bg="Red")
button1.pack(side=LEFT)




main_menu = Menu(root)
root.config(menu=main_menu)


sub_menu = Menu(main_menu)

main_menu.add_cascade(label="File", menu=sub_menu)
sub_menu.add_command(label="New", command=function1)
sub_menu.add_command(label="Save", command=function2)

sub_menu.add_separator()
sub_menu.add_command(label="Open", command=function1)

second_menu = Menu(main_menu)
main_menu.add_cascade(label="Edit", menu=second_menu)
second_menu.add_command(label="Undo", command=function1)

third_menu = Menu(main_menu)
main_menu.add_cascade(label="View", menu=third_menu)
third_menu.add_command(label="Context Files", command=function1)


toolbar = Frame(root, bg='pink')
button1 = Button(toolbar, text="Undo", command=function1)
button1.pack(side=LEFT, padx=2, pady=3)

button2 = Button(toolbar, text="Redo", command=function1)
button2.pack(side=LEFT, padx=2, pady=3)

toolbar.pack(side=TOP, fill=X)

status_bar = Label(root, text="current status of the file", bd=1, relief=SUNKEN, anchor=W)
status_bar.pack(side=BOTTOM, fill=X)


import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo("Dialog Box", "File is ready for use")
response = tkinter.messagebox.askquestion("Question1", "Do you want to save file?")
if response == "yes":
    print("The file is saved")
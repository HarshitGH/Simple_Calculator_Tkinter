# p = int(input('enter value of p'))
# r = int(input('enter value of r'))
# t = int(input('enter value of t'))
#
# SI = (p*r*t)/100
#
# print("The simple interest is {}".format(SI))

# age = int(input("Enter your age "))
#
# if age < 18:
#     print('Applicant is a Minor')
# elif 18 < age < 50:
#     print('Applicant is an adult')
# else:
#     print('Applicant is an old man')


# l1 = [2, 3, 4, 5]
# l2 = [3, 5, 7, 9]
# l3 = (l1 + l2)
# print(l3*2)


# fruits = ['apple', 'mango', 'papaya', 'banana']
# fruits.insert(1, 'peach')
# print(fruits.index('mango'))


# numbers = list(range(20))
# print(numbers)
#
# numbers2 = list(range(5, 25, 3))
# print(numbers2)


# for x in range(1, 10):
#     if x % 2 == 0:
#         print('even number')
#     else:
#         print('odd number')


# username = 'harshitpadaliya5'
# password = '123456'
#
# if username == 'harshitpadaliya5' and password == '123456':
#     print('Valid user')
# else:
#     print('invalid user')

# counter = 0
# while counter <= 10:
#     print(counter)
#     counter += 1

# food = ['rajma', 'chole bhature', 'dal', 'curd', 'egg']
# print(food[2])
# food.append('roti')
# food.insert(2, 'tacos')
# print(food)


# def squares():
#     for i in range(10):
#         print(i**2)
# print(squares())


# def add(a, c):
#     b = (a + c)
#     return b
#
#
# result = add(3056, 9876)
# print(result)


# def add(a, b):
#     return a + b
#
# def squares(c):
#     return c ** 2
#
# result = squares(add(34,56))
# print(result)

# import random
#
# for x in range(5):
#     result = random.randint(1, 10)
#     print(result)


# weight = float(input('Enter your weight in kgs '))
# height = float(input('Enter your height in meters'))
#
# bmi = weight/(height*2)
# print('Your current bmi is {}'.format(bmi))
# try:
#     a = 20
#     b = 0
#     print(a/b)
# except ZeroDivisionError:
#     print('there is a division by zero error')
# finally:
#     print('my name is expert programmer')


# demofile = open('demo.txt', 'w')
# demofile.write("hi my name is tamanna\ni am very very cute")
# demofile.close()
#
#
# demofile = open('demo.txt', 'a')
# demofile.write('\nI like chole bhature')
# demofile.close()
#
# demofile = open('demo.txt', 'r')
# contents = demofile.read()
# print(contents)
# demofile.close()
#
# def divide(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         print('cannot divide by zero')
#         return 0
#
#
#
# x = float(input('Enter first value'))
# y = float(input('enter number to be divided by'))
#
# result = divide(x, y)
# print(result)

# new_dict = {'orange': 32, 'apple': 54, 'guava': 76}
# print(new_dict['orange'])
#
# print(new_dict.get('guava'))
#
#
# print(new_dict.get('banana','out of stock'))


# LIST COMPREHENSIONS
# value = [x**3 for x in range(10) if x % 2 != 0]
# print(value)

# STRING FUNCTIONS
# x = '|'.join(['apple', 'mango','papaya'])
# print(x)


# y = 'hello world'.replace('world', 'there')
# print(y.lower())


# x = list(range(10))
# print(max(x))

# product = {'lock': 23, 'key': 34, 'chair': 54, 'dine': 87, 'table': 99}
# product_name = input('Enter the name of product ')
# if product_name in product:
#     print(product.get(product_name))
# else:
#     print('no product found')


# z =[x for x in range(1, 101) if x % 2 != 0]
# print(z)

# print((lambda x: x**2)(35))
# result = (lambda z: z*40)(50)
# print(result)
# Lambda functions are called as anonymous functions


# def add(x):
#     return x + 2
#
# # MAPS IN PYTHON
# newlist = [23, 65, 76, 89]
# result = list(map(add, newlist))
# print(result)
#
#
# newlist = [23, 65, 76, 89]
# result = list(map(lambda x: x+2, newlist))
# print(result)
# FILTERS IN PYTHON
# newlist = list(range(30))
# result = list(filter(lambda x: x % 2 == 0, newlist))
# print(result)

# def student_discount(p):
#     discounted_student_price = p - (p/10)
#     return discounted_student_price
#
#
# def regular_buyer_discount(p):
#     discounted_regular_buyer_price = p - (p/20)
#     return discounted_regular_buyer_price
#
# price = 100
# Final_price = regular_buyer_discount(student_discount(price))
# print(Final_price)

# print((lambda x: x*(x+5)**2)(5))
price_list =[23, 56, 78, 98, 104]

discounted_price = list(map(lambda x:x-x/10, price_list))
print(discounted_price)
















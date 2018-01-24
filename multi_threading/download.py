# import json
# import logging
# import sys
# from urllib
import time
import threading

# logger = logging.getLogger(__name__)

# def get_links(client_id):
#    headers = {'Authorization': 'Client-ID {}'.format(client_id)}
#    req = Request('https://api.imgur.com/3/gallery/', headers=headers, method='GET')
#    with urlopen(req) as resp:
#        data = json.loads(resp.readall().decode('utf-8'))
#    return map(lambda item: item['link'], data['data'])

# def download_link(directory, link):
#    logger.info('Downloading %s', link)
#    download_path = directory / os.path.basename(link)
#    with urlopen(link) as image, download_path.open('wb') as f:
#        f.write(image.readall())

# def setup_download_dir():
#    download_dir = Path('images')
#    if not download_dir.exists():
#        download_dir.mkdir()
#    return download_dir


# Multithreading Basics

# functions without multithreading
# def calc_square(numbers):
#     print "Calculate the square numbers"
#     for n in numbers:
#         time.sleep(0.2)
#         print "square", n * n

# def calc_cube(numbers):
#     print "Calculate, the cube numbers"
#     for n in numbers:
#         time.sleep(0.2)
#         print "cube", n * n * n

# arr = [2, 3, 8 , 9]
# t = time.time()
# calc_square(arr)
# calc_cube(arr)
# print "Done in : ", time.time() - t
# print "Ha, I am done with all my work now"
# process time is 1.6s

# response 
'''
Calculate the square numbers
square 4
square 9
square 64
square 81
Calculate, the cube numbers
cube 8
cube 27
cube 512
cube 729
Done in :  1.60218095779
'''


''' Function with multithreading
finished with
'''

# def calc_square(numbers):
#     print "Calculate the square numbers"
#     for n in numbers:
#         time.sleep(0.2)
#         print "square", n * n

# def calc_cube(numbers):
#     print "Calculate, the cube numbers"
#     for n in numbers:
#         time.sleep(0.2)
#         print "cube", n * n * n

# arr = [2, 3, 8 , 9]
# thread_one = threading.Thread(target=calc_square, args=(arr,))
# thread_two = threading.Thread(target=calc_cube, args=(arr,))

# thread_one.start()
# thread_two.start()

# thread_one.join()
# thread_two.join()

'''
#  Respoinse 

Calculate the square numbers
 Calculate, the cube numbers
cubesquare  4
8
cubesquare 27
 9
cubesquare 512 64

cube 729
square 81
[Finished in 0.8s]
'''
# print calc_square(arr)
# print calc_cube(arr)



'''
Getters and setter
'''

# class Employee:

#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last + '@email.com'


#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)

# emp_1 = Employee('Kennedy', 'Anyinatoe')

# print emp_1.first
# print emp_1.last
# print emp_1.email
# print emp_1.fullname()

'''
Learn how to write code on white paper
be able to write conditional statements
talk about ur past projects (web scrapping, scrap the weather everyday)
learn how to write some code like fibonacci and FIZBUZZ problems
why would u you a tuple instead of a list
learn about the data types and how to iterate them 
Dictionary being a hash table and what it means 
KNow how to use list comprehensions
Know how to use Generators use yield and next
a, b = 0, 1
for i in xrange(0, 10):
    print a
    a, b = b, b + a
'''


# def square_numbers(nums):
#     for i in nums:
#         yield(i * i)
    


# numbers = square_numbers([1,2,3,4,5])

# # print 'the numbers are ', next(numbers)

# for num in numbers:
#     print num


# my_num = [x *x for x in [1,2,3,4,5]]
# print my_num

# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart

# x = Complex(3.0, -4.0)
# print x.r 
# print x.i

# class MyClass:
#     i = 12345

#     def f(self):
#         return 'hello world'
# x = MyClass()
# print x.f()
# x.counter = 1

# while x.counter < 10:
#     x.counter = x.counter * 2
# print x.counter

# class Dog:

#     def __init__(self, name):
#         self.name = name
#         self.tricks = []

#     def add_tricks(self, trick):
#         self.tricks.append(trick)
# a = Dog('Richie')
# b = Dog('Nash')
# print a.name
# print '\n'
# print b.name
# print '\n'
# a.add_tricks('saying hello')
# b.add_tricks('hello back')

# c = a.tricks + b.tricks
# print c







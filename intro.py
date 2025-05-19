from __future__ import print_function
import fibo
import fibo as fb
import platform
from mod import greeting
from mod import person1

# Basic Syntax
name = 'Wariz'
print(name)


# Variables and Data types
x = 5
print(x)

a = str(3)
b = int(3)
c = float (3)

print(type(a))
print(type(b))
print(type(c))

d = 4
D = 'Sallly'

print(d)
print(D)

e, f, g = 'Orange', 'Banana', "Cherry"
print(e)
print(f)
print(g)

h = i = j = 'Orange'
print(h)
print(i)
print(j)

fruits = ['apple', 'banana', 'cherry']
k, l, m = fruits
print(k)
print(l)
print(m)

n = "Python"
o = 'is'
p = 'awesome'

print (n, o, p)
print (n + o + p)

q = 5
r = 'John'
print(q, r)

s = 'awesome'

def myFunc():
  s = 'fantastic'
  print('Python is ' + s)

myFunc()

print('Python is ' + s)

def myfunc():
    global t
    t = 'fantastic'

myfunc()
print('Python is ' + t)


# Data Types

u = 'Hello Wariz'  # string
v = 20 # int
w = 20.5  # float
x = 1j  # complex
x = ['apple', 'banana', 'cherry']   # list
x = ('apple', 'banana', 'cherry')   #tuple
x = range(6)  # range
x = {'name': 'John', 'age': 36}   # dict
x = {'apple', 'banana', 'cherry'}   # set
x = frozenset({'apple', 'banana,' 'cherry'})    # frozenset
x = True  # bool
x = b'hello' # bytes
x = bytearray(5)    # bytearray
x = memoryview(bytes(5))    # memeryview
x = None  #nonetypes


# Conditionals

conditionX = 0
conditionY = 5

if conditionX < conditionY:
   print('yes')

if conditionY < conditionX:
    print('yes')

if conditionX:
    print('yes')

if conditionY:
    print('yes')


name = ''

if name == 'Joe':
    print('Hello Joe')
elif name == 'Wariz':
    print('Hello Wariz')
elif name == 'Sally':
    print('Hello Sally')
elif name == 'Dimeji':
    print('Hello Dimeji')
else:
    print('I dont know you')

if 'foo' in ['bar', 'baz', 'qux', 'foo']:
    print('Expression is true')
    print('Executing statement in suite')
    print('...')
    print('Done')
print('After conditional')

if 'wariz' in ['wariz', 'samad']:
    print('Outer condition is true')

    if 10 > 20:
        print('inner condition 1')

    print('Between inner conditions')

    if 10 < 20:
        print('Inner condition 2')

    print('End of outer condition')

print('After outer condition')


if 'f' in 'foo': print(1); print(2); print(3)

# Python ternary operator

raining = False
print('lets go to the', 'beach' if raining else 'library')

raining = True
print('lets go to the', 'beach' if  raining else 'library')

age = 12
s = 'minor' if age < 21 else 'adult'
print(s)

if True:
    pass

print('foo')


# match case statement

command = ''

match command:
    case 'Hello, World':
        print('Hello to you too!')
    case 'Goodbye, World!':
        print('See you later!')
    case other:
        print('No match found')


# Loops in python

# while loops

cnt = 0
while (cnt < 3):
    cnt = cnt + 1
    print('Hello Geek')
    print(cnt)


# while loop with else statement

cn = 0
while (cn < 3):
    cn = cn + 1
    print('Hello Geek')
else:
    print('In else block')



# for loop

n = 4

for i in range(0, n):
    print(i)


li = ['geeks', 'for', 'geeks']

for i in li:
    print(i)


tup = ('geeks', 'for', 'geeks')
for i in tup:
    print(i)


s = 'geek'
for i in s:
    print(i)

d = dict({'x': 123, 'y': 345})

for i in d:
    print('%s   %d' % (i, d[i]))


set1 = {1, 2, 3, 4, 5, 6}

for i in set1:
    print(i)

lists = ['geek', 'for', 'geek']

for index in range(len(lists)):
    print(lists[index])



for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()


# Continue statement

for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print('Current letter:', letter)

for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        break
print('Current letter :', letter)


for letter in 'geeksforgeeks':
    pass
print('Last Letter :', letter)


n = 5

while n > 0:
    n -= 1
    print(n)


# type conversion

# implicit type conversion
integer_number = 123
float_number = 1.23

new_number = integer_number + float_number

print('Value:', new_number)
print('Data type:', type(new_number))

# explicit type conversion

num_string = '12'
num_integer = 23

print('Data type of num_string before Type casting:', type(num_string))

# explicit conversion

num_string = int(num_string)

print('Data type of num_string after type casting:', type(num_string))

NUM_SUM = num_integer + num_string

print('Sum:', NUM_SUM)
print('Data type of NUM_SUM:', type(NUM_SUM))



# Error handling
# view all built-in exceptions
print(dir(locals()['__builtins__']))


# exception handling

try:
    numerator = 10
    denominator = 0

    result = numerator / denominator
    print(result)

except:
    print('Error: Denominator cannot be 0.')


try:

    even_number = [2, 4, 6, 8]
    print(even_number[5])
except ZeroDivisionError:
    print('Denominator cannot be 0.')
except IndexError:
    print('Index out of range.')

# try with else clause

# try:
#     num = int(input('Enter a number: '))
#     assert num % 2 == 0
# except: 
#     print('Not an even number!')
# else:
#     reciprocal = 1 / num
#     print('Reciprocal:', reciprocal)


# try with finally clause

try:
    numerator = 10
    denominator = 0

    result = numerator / denominator
    print(result)
except:
    print('Error: Denominator cannot be 0.')
finally:
    print('This is finally block.')



# Functions

def greet(name):
    print('Hello', name)
    print(f'Hello {name} Kolapo')

greet('Wariz')

def abs (num):
    # return num if num > 0 else -num

    if num > 0:
        return num
    else:
        return -num

print(abs(10))
print(abs(-10))


# Arbitrary arguments

def my_function(*kids):
    print('The youngest child is ' + kids[1])

my_function('Emil', 'Tobias', 'Linus')


# Keyword arguments

def keyword_function(child3, child2, child1):
    print('The youngest child is '  + child3)
    print('The youngest child is '  + child2)
    print('The youngest child is '  + child1)


keyword_function(child1='Wariz', child2='Samad', child3='Kolapo')

# Arbitrary keyword arguments

def arbitrary_keyword_function(**kid):
    print('His last name is ' + kid['lname'])

arbitrary_keyword_function(fname = 'James', lname = 'Bond')


# Default parameter value

def default_function(country = 'Norway'):
    print('I am from ' + country)

default_function('Sweden')
default_function('Senegal')
default_function()
default_function('Nigeria')


# Passing a list as an argument

def list_function(food):
    for x in food:
        print(x)

fruits = ['apple', 'banana', 'cherry']

list_function(fruits)


# Return values

def return_function(x):
    return 5 * x


print(return_function(5))

# The pass statement

def pass_function():
    pass

print(pass_function())


# Positional-only Arguments

def positional_function(x, /):
    print(x)

positional_function(3)

def positional_function2(x):
    print(x)

positional_function2(x = 3)


# def positional_function3(x, /):
#     print(x)

# positional_function3(x = 3)

# Keyword only Arguments

def keyword_only_function(*, x):
    print(x)

keyword_only_function(x = 7)


def positional_and_keyword_function(a, b, /, *, c, d):
    print(a + b + c + d)

positional_and_keyword_function(5, 6, c = 7, d = 8)


# Recursion

def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0

    return result

print('Recursion Example Results:')
tri_recursion(5)


# Lists

x_list = [1, 3, 3, 7]
print(type(x_list))
print(x_list)
x_tuple = (1, 3, 3, 7)
print(type(x_tuple))
print(x_tuple)
x_set = {1, 3, 3, 7}
print(type(x_set))
print(x_set)


color = ['blue', 'green', 'red', 'yellow']
fruit = ['blueberry', 'apple', 'cherry', 'banana']


# df = pd.DataFrame(columns=['color', 'fruit'])

# df['color'], df['fruit']= color, fruit

# print(df)


# Tuples

t = 12345, 54321, 'hello'
print(t[0])
print(t)

u = t, (1, 2, 3, 4, 5)
print(u)

# t[0] = 8888
# print(t)

p, q, r = t
print(p)
print(q)
print(r)


first, *second = t
print(first)
print(second)


# Sets

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}


# Set Union
print(A.union(B))
print(A | B)


# Set intersection
print(A.intersection(B))
print(A & B)

# Set difference
print(B.difference(A))
print (B - A)

# Set symemetric difference
print(A.symmetric_difference(B))


this_set = {'apple', 'banana', True, False, 1, 0}
print(this_set)


print(len(this_set))
print(type(this_set))


set_constructor = set(('apple', 'cherry', 1, True, False, 0, 32))
print(set_constructor)


# Dictionary

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])
del tel['sape']
print(tel)
tel['irv'] = 4127
print(tel)
print(sorted(tel))
print(list(tel))

print('guido' in tel)

print('jack' not in tel)

dicts = dict([('sape', 4), ('wariz', 'samad')])
print(dicts)

print({x: x**2 for x in (2, 4, 6)})


# Looping dict

knights = {'gallahad': 'the pure', 'robin': 'the brave'}

for k, v in knights.items():
    print(k + '----------------- ' + v)

for i, j in enumerate(['tic', 'tac', 'toe']):
    print(i, j)

for k, l in enumerate(knights):
    print(k, l)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print(q, a)
    print('What is your {0}? It is {1}.'.format(q, a))

for i in reversed(range(1, 10, 2)):
    print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

for i in sorted(basket):
    print(i)

for j in sorted(set(basket)):
    print(j)


import math

raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5,float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        print(value)
        filtered_data.append(value)


print(filtered_data)


# Modules

result1 = fibo.add(10, 5)
print('result from fibo add function = ', result1)

# Renaming a module
result2 = fb.sub(10, 5)
print('result from fb sub function = ', result2)


x = platform.system()
print(x)

y = platform.python_version()
print(y)

z = dir(platform)
print(z)


# Import from module

print(greeting('Wariz'))
print(person1)
print(person1['age'])


# Lambda function

lam_A = lambda a : a + 10
print(f'Lambda function = {lam_A(5)}')

lam_B =lambda a, b: a * b
print(f'Lambda function 2 = {lam_B(5, 2)}')

# Power of lambda

def lam_C (n):
    return lambda a : a * n

mydoubler = lam_C(5)
print(mydoubler(4))


def lam_C ():
    return lambda a: a + 4

double = lam_C()
print(double(3))

print((lambda x: x * 2)(2))

fullname = lambda first, second: f'Full name: {first.upper()} {second}'
print(fullname('wariz', 'kolapo'))


def my_map(my_func, my_iter):
    result = []
    for item in my_iter:
        new_item = my_func(item)
        result.append(new_item)
    return result

nums = [3, 4, 5, 6, 7]

cubed = my_map(lambda x: x**3, nums)
print(cubed)

# Decorators
# function decorators

import functools

def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5

result = add5(10)
print(result)
print(help(add5))
print(add5.__name__)


def repeat(num_times):

    def decorator_repeat(func):
        @functools.wraps(func)

        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=4)
def greet(name):
    print(f'Hello {name}')

greet('Wariz')
greet('Kolapo')

def start_new_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start of function')
        result = func(*args, **kwargs)
        print('End of function')
        return result
    return wrapper


def debug(func):
    @functools.wraps(func)

    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f'{func.__name__} returned {result!r}')
        return result
    return wrapper


@debug
@start_new_end_decorator
def say_hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting

say_hello('Idan mi')

# Class decorators

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwds):
        self.num_calls += 1
        print(f'This is executed {self.num_calls} times')
        return self.func(*args, **kwds)

@CountCalls

def say_hello2():
    print('Hello!')

say_hello2()
say_hello2()

# Function decorator time

import time

def tictoc (func):

    def wrapper():
        start = time.time()
        func()
        end = time.time() - start
        print(f'{func.__name__} ran in {end} seconds')
    return wrapper

@tictoc

def do_this():
    time.sleep(1.3)

@tictoc

def do_that():
    time.sleep(2.5)

do_this()
do_that()
print('Done!')

# Iterators

mytuple = ('apple', 'banana', 'cherry')
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mystr = 'banana'
myit2 = iter(mystr)

print(next(myit2))
print(next(myit2))
print(next(myit2))
print(next(myit2))
print(next(myit2))
print(next(myit2))

for x in mytuple:
    print(x)

for x in mystr:
    print(x)


# Class Iterator

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


# Class Iterator with stopiteration

class MyNumbers2():
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
        

myclass2 = MyNumbers2()
myiter2 = iter(myclass2)

for x in myiter2:
    print(x)


# Regular Expressions

import re

txt = 'The rain in Spain'
xy = re.search("^The.*Spain$", txt)
print(xy)

print(re.findall('pa', txt))

print(re.search('\s', txt))
print(re.search('jdf', txt))

print(re.split('\s', txt, 1))
print(re.split('\s', txt, 2))

print(re.sub('\s', '9', txt))
print(re.sub('\s', '9', txt, 2))

xk = re.search(r"\bS\w+", txt)
print(xk.span())
print(xk.string)
print(xk.group())



# Object Oriented Programming OOP

class Dog:
    species = 'Canis familiaris'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__ (self):
        return f"{self.name} is {self.age} years old"

    def speak (self, sound):
        return f"{self.name} says {sound}"
    

miles = Dog('Miles', 4)
print(miles.name)
print(miles.age)
print(miles.species)
miles.species = 'Felis silvestris'
print(miles.species)
print(miles.__str__())
print(miles.speak('Woof woof'))
print(miles)


# Exercise

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    
    def __str__ (self):
        return f"The {self.color} car has {self.mileage} miles."
    
        
blue = Car('blue', 20000)
red = Car('red', 30000)

print(blue)
print(red)

for car in (blue, red):
    print(car)

class DogNew:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


jack = DogNew("Jack", 3, "Bulldog")
jim = DogNew("Jim", 5, "Bulldog")

print(jack.speak("Woof"))
print(jim.speak("Woof"))

class NewDog2:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} barks: {sound}"


class JackRussellTerrier(NewDog2):
    def speak(self, sound='Arf'):
        return f"{self.name} says {sound}"

class Dachshund(NewDog2):
    def speak(self, sound='Arfff'):
        return super().speak(sound)

class Bulldog(NewDog2):
    pass

miless = JackRussellTerrier("Miless", 4)
buddys = Dachshund("Buddy", 9)
jacks = Bulldog("Jack", 3)
jims = Bulldog("Jim", 5)

print(miless.species)
print(type(miless))
print(isinstance(miless, NewDog2))
print(isinstance(miless, Bulldog))
print(isinstance(jack, Dachshund))

print(miless.speak())
print(miless.speak('Grrr'))
print(jims.speak('Woof'))

print(buddys.speak())

class TheDog:
    species = 'Canis familiaris'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self, sound):
        return f'{self.name} says {sound}'


class GoldenRetriever(TheDog):
    def speak(self, sound='Bark'):
        return super().speak(sound)

warizDog = GoldenRetriever('Jacker', 10)
print(warizDog.speak())



# Dates

import datetime

dateX = datetime.datetime.now()
print(dateX)
print(dateX.year)
print(dateX.strftime('%A'))
print(f"Strftime output: {dateX.strftime('%B')}")
print(dateX.strftime('%c'))

dateY = datetime.datetime(2020, 5, 17)
print(dateY)

dateZ = datetime.datetime(2018, 6, 1)
print(dateZ.strftime('%w'))

# Math

import math

mathX = math.sqrt(64)
print(mathX)

mathY = math.ceil(1.4)
print(mathY)

mathZ = math.floor(1.4)
print(mathZ)

mathPi = math.pi
print(mathPi)


# JSON

import json

# convert from json to python. Result is a python dictionary
jsonX = '{"name": "John", "age": 30, "city": "New York"}'
jsonY = json.loads(jsonX)
print(jsonY)
print(jsonY['city'])

# convert from python to json. Result is a json string

jsonZ = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

jsonA = json.dumps(jsonZ)
print(jsonA)

# convert python object into JSON strings

print(json.dumps({'name': 'John', 'age': 30}))
print(json.dumps(['apple', 'banana']))
print(json.dumps(('apple', 'banana')))
print(json.dumps('Hello'))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


jsonB = {
    'name': 'John',
    'age': 30,
    'married': True,
    'divorced': False,
    'children': ('Ann', 'Billy'),
    'pets': None,
    'cars': [
        {'model': 'BMW 230', 'mpg': 27.5},
        {'model': 'Ford Edge', 'mpg': 24.1}
    ]
}

print(json.dumps(jsonB))

# Formatting json result

print(json.dumps(jsonB, indent=4))
print(json.dumps(jsonB, indent=4, separators=('. ',' = ')))
print(json.dumps(jsonB, indent=4, sort_keys=True))

# PIP

# import camelcase

# camelcaseA = camelcase.CamelCase()

# txt = 'hello world'
# print(camelcaseA.hump(txt))
# print(camelcaseA.stop_words)


# String formatting

formatA = 59
formatTxt = f'The price is {formatA:.2f} dollars'
print(formatTxt)

formatB = f'The price is {95:.2f} dollars'
print(formatB)

# Perform if...else statement

formatPrice = 492

formatC = f'It is very {'Expensive' if formatPrice > 50 else 'cheap'}'
print(formatC)

formatFruit = 'apples'
formatD = f'I love {formatFruit.upper()}'
print(formatD)

formatPrice2 = 59000

print(f'the price is {formatPrice2:_} dollars')

# User Input

print('Enter your name:')
inputName = input()
print(f'Hello {inputName}')

inputName2 = input('Enter your name: ')
print(f'Hello {inputName2}')

inputName3 = input("Enter your inputName3:")
print(f"Hello {inputName3}")
fav1 = input("What is your favorite animal:")
fav2 = input("What is your favorite color:")
fav3 = input("What is your favorite number:")
print(f"Do you want a {fav2} {fav1} with {fav3} legs?")


# input number
import math

inputNumber = input('Enter a number: ')

inputY = math.sqrt(float(inputNumber))
print(f'The square root of {inputNumber} is {inputY}')

formatY = True

while formatY == True:
    x = input('Enter a number:')
    try:
        x = float(x)
        formatY = False
    except:
        print('Wrong input, please try again')

print('Thank you')

# Package managers
#pip
# pip install camelcase
# pip install requests
# pip install pandas

# uv


# Common packages

# requests

# File handling

3# Open a file

fileF = open('demofile.txt')
print(fileF.read())


# Using the with statement. Using with takes care of manually closing the file

with open('demofile.txt') as fileJ:
    print(fileJ.read())

# Closing a file
fileF = open('demofile.txt')
print(fileF.readline())
print(fileF.readline())
fileF.close()

# Reads the first 5 characters of the file
with open('demofile.txt') as fileJ:
    print(fileJ.read(5))

# Readline reads the first lines of the file
with open('demofile.txt') as fileJ:
    print(fileJ.readline())


with open('demofile.txt') as fileJ:
    for x in fileJ:
        print(x)

# Writing to an existing file

# 'a' - Append - will append to the end of the file
with open('demofile.txt', 'a') as fileJ:
    fileJ.write('Now the file has more content!')

with open('demofile.txt') as fileJ:
    print(fileJ.read())

# 'w' - Write - will overwrite the entire file
with open('demofile.txt', 'w') as fileJ:
    fileJ.write('Woops! I have deleted the content!')

with open('demofile.txt') as fileJ:
    print(fileJ.read())



# Creating a new file

# 'x' - Create - will create a file, returns an error if the file exists
with open('myfiles.txt', 'a') as fileJ:
    fileJ.write('This is my new file!')


# Delete a file
import os
# os.remove('myfiles.txt')

# Check if file exists
if os.path.exists('myfiles.txt'):
    os.remove('myfiles.txt')
else:
    print('The file does not exist')

# Delete a folder
# os.rmdir('myfolder')
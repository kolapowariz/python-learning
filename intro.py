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
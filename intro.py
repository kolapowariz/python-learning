from __future__ import print_function
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

list = ['geek', 'for', 'geek']

for index in range(len(list)):
    print(list[index])



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

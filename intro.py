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
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

for x in car.items():
  print(x)


my_list = [1, 3, 'a']
print(dir(my_list))
print(17 ** 3)

my_list = [0, 1, 2, 3, 4, ['a', 'b', ['c']], 'penultimate', 6]
print(my_list[:3])
print(my_list[-2])
print(my_list[-3][1])


def multiplication (first, second):
  return first * second

print(multiplication(3, 4))

def is_even (value):
  if (value % 2 != 0):
    return False
  
  return True

print(is_even(0))

even_list = []
odd_list = []
for x in range(0, 21):
  if is_even(x):
    even_list.append(x)
    print(x)
    print(even_list)
  else:
    odd_list.append(x)
    print(odd_list)
    print('Not an even number')
    
  
print(even_list)
print(odd_list)


def trigger_alarm(sensor_data, alarm_limit):
  for x in sensor_data:
    if (x < alarm_limit):
      print('Normal')
    else: 
      print('Alarm!!!')


sensor_data = [1.2, 3, 4.1, 2.2, 5, 6, 1, 4]
alarm_limit = 4
trigger_alarm(sensor_data, alarm_limit)



def weekly_production (production_list):
  
  total_week = 0

  for production_day in production_list:
    total_week += production_day
  
  mean = total_week / len(production_list)

  return total_week, mean


production_list = [230, 254, 214, 208, 235, 120]

print(weekly_production(production_list))
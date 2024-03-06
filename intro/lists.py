my_list = [1, 2, 3, 4, 5]
if len(my_list) > 3:
  print('list is pretty long')
else:
  print('list is pretty short')
my_list.append(6)
print(my_list)
my_list.append([7, 8])
print(my_list)
my_list.extend([9, 10])
print(my_list)
print(my_list[5])
print(my_list[5:8])
print(my_list[3:])
print(my_list[:4])
print(my_list[:])
print(my_list[:-1])
for item in my_list:
  print(item, end='')
for index, item in enumerate(my_list):
  print('at {i} element {e}'.format(i = index, e = item))
del my_list[6]
print(my_list)
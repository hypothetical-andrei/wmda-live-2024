my_dog = {
  'name': 'spot',
  'weight': 20,
  'color': 'breen'
}

print(my_dog)

for k, v in my_dog.items():
  print(k, ' ', v)

if 'read_counter' in my_dog:
  my_dog['read_counter'] = my_dog['read_counter'] + 1
else:
  my_dog['read_counter'] = 1
# my_dog.setdefault('read_counter', 1)

print(my_dog)

my_tuple = (1, 'a')
print(my_tuple)
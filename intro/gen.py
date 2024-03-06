def gen_stuff():
  for i in range(0, 9):
    yield i


for element in gen_stuff():
  print(element)
def my_function(a, b, c, d = 3, e = 3):
  return a + b + c + d + e, a + b + c

print(my_function(1, 2, 3, 4, 5))

first, all = my_function(1, 2, 3, 4, 5)
print(first)
print(all)

f1 = lambda x: x * 2
my_list = [1, 2, 3, 4, 5]
print(list(map(f1, my_list)))
print(list(map(lambda x: x * 3, my_list)))

second_list = [ x * 2 if x > 3 else 0 for x in my_list ]
print(second_list)
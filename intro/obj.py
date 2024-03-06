class MyClass():
  def __init__(self, content):
    self.content = content
  def __repr__(self):
    return 'my content is {c}'.format(c = self.content)

my_obj = MyClass('some content')

print(my_obj)
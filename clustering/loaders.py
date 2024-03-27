def load_blog_data(filename='./blogdata.txt'):
  with open(filename) as f:
    lines = f.readlines()
  col_names = lines[0].strip().split('\t')[1:]
  row_names = []
  data = []
  for line in lines[1:]:
    parts = line.strip().split('\t')
    row_names.append(parts[0])
    data.append([float(x) for x in parts[1:]])
  return col_names, row_names, data

def main():
  col_names, row_names, data = load_blog_data()
  print(col_names[:3])
  print(row_names[:3])
  print(data[:3])

if __name__ == '__main__':
  main()

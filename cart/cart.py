import loaders
from math import log
import random

def unique_counts(rows):
  results = {}
  for row in rows:
    outcome = row[-1]
    results.setdefault(outcome, 0)
    results[outcome] += 1
  return results

def entropy(rows):
  log2 = lambda x: log(x) / log(2)
  results = unique_counts(rows)
  h = 0.0
  for result, count in results.items():
    p = float(count / len(rows))
    h -= p * log2(p)
  return h

class DecisionNode:
  def __init__(self, col=-1, value=None, results=None, false_subtree = None, true_subtree = None):
    self.col = col
    self.value = value
    self.results = results
    self.false_subtree = false_subtree
    self.true_subtree = true_subtree

def divide_sets(rows, column, value):
  split_function = None
  if isinstance(value, int) or isinstance(value, float):
    split_function = lambda row: row[column] >= value
  else:
    split_function = lambda row: row[column] == value
  true_set = [row for row in rows if split_function(row)]
  false_set = [row for row in rows if not split_function(row)]
  return (false_set, true_set)

def build_tree(rows):
  if len(rows) == 0:
    return DecisionNode()
  current_score = entropy(rows)
  best_gain = 0.0
  best_criterion = None
  best_sets = None
  column_count = len(rows[0]) - 1
  for column in range(0, column_count):
    column_values = {}
    for row in rows:
      column_values[row[column]] = 1
    for value in column_values.keys():
      (false_set, true_set) = divide_sets(rows, column, value)
      p = float(len(false_set) / len(rows))
      gain = current_score - p * entropy(false_set) - (1 - p) * entropy(true_set)
      if gain > best_gain and len(false_set) > 0:
        best_gain = gain
        best_criterion = (column, value)
        best_sets = (false_set, true_set)
  if best_gain > 0.0:
    false_branch = build_tree(best_sets[0])
    true_branch = build_tree(best_sets[1])
    return DecisionNode(col=best_criterion[0], value=best_criterion[1], true_subtree=true_branch, false_subtree=false_branch)
  else:
    return DecisionNode(results=unique_counts(rows))

def print_tree(node, indent = ''):
  if node.results != None:
    print(node.results)
  else:
    print(node.col, ':', node.value, '?')
    print(indent, 'True -> ', end='')
    print_tree(node.true_subtree, indent=indent + '  ')
    print(indent, 'False -> ', end = '')
    print_tree(node.false_subtree, indent=indent + '  ')

def classify(item, node):
  if node.results != None:
    return node.results
  else:
    value = item[node.col]
    if isinstance(value, int) or isinstance(value, float):
      if value >= node.value:
        print(f'decision {node.col} >= {value}')
        branch = node.true_subtree
      else:
        print(f'decision {node.col} < {value}')
        branch = node.false_subtree        
    else:
      if value == node.value:
        print(f'decision {node.col} == {value}')
        branch = node.true_subtree
      else:
        print(f'decision {node.col} != {value}')
        branch = node.false_subtree
    return classify(item, branch)     

def main():
  data = loaders.get_car_data()
  random.shuffle(data)
  test_data = data[:100]
  train_data = data[100:]
  tree = build_tree(train_data)
  # print_tree(tree)
  correct_count = 0
  for item in test_data:
    result = classify(item, tree)
    if item[-1] in result and len(result.keys()) == 1:
      correct_count += 1
  print(f"{correct_count} / 100")

if __name__ == '__main__':
  main()
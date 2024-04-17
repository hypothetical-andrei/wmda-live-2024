import loaders
from math import log

def unique_counts(rows):
  results = {}
  for row in rows:
    outcome = row[-1]
    results.setdefault(outcome, 0)
    results[outcome] += 1
  return results

def entropy(row):
  pass
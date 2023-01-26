import random
import numpy as np
from tqdm import tqdm
def convergence_test_vectorized(algo,N,nums=None):
  D = algo.getD()
  if nums is None:
    nums = []
    MAX_NUM = 2000
    MIN_NUM = 1000
    for d in D:
      nums.append(random.randint(MIN_NUM,MAX_NUM))
  total = np.array(nums).sum()
  totals = np.array([0.0 for _ in D])
  for _ in tqdm(range(N)):
    results = {}
    for d in D:
      results[d]=0
    for d in D:
      for _ in range(nums[d]):
        res = algo.f(d)
        for i in D:
          results[i]+=res[i]
    estims = np.array(list(algo.g(results,total).values()))
    totals +=estims
  return totals/N,nums

def convergence_test_non_vectorized(algo,N,nums=None):
  D = algo.getD()
  if nums is None:
    nums = []
    MAX_NUM = 2000
    MIN_NUM = 1000
    for d in D:
      nums.append(random.randint(MIN_NUM,MAX_NUM))
  total = np.array(nums).sum()
  totals = np.array([0.0 for _ in D])
  for _ in tqdm(range(N)):
    results = {}
    for d in D:
      results[d]=0
    for d in D:
      for _ in range(nums[d]):
        results[algo.f(d)]+=1
    estims = np.array(list(algo.g(results,total).values()))
    totals +=estims
  return totals/N,nums
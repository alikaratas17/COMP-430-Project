from LDP_Algorithms import GRR
from tqdm import tqdm
import numpy as np

EPSILON = 1.0
MIN_AMOUNT = 10000
MAX_AMOUNT = 20000
LEN_D = 10
SKIP_FIRST = True
SKIP_SECOND = False
SKIP_THIRD = True
AMOUNT = 10000

grr = GRR.GRR(EPSILON,LEN_D)
D = grr.getD()

if not SKIP_FIRST:
  amounts = {}
  for d in D:
    amounts[d] = np.random.randint(MIN_AMOUNT,MAX_AMOUNT)
  print("\n\n"+"-"*10+"Starting First Experiment")
  results = []
  for d in tqdm(D):
    for _ in range(amounts[d]):
      results.append(grr.f(d))
  results = np.array(results)
  accumulations = {}
  for d in D:
    accumulations[d] = (results==d).sum()
  predictions = grr.g(accumulations)
  for d in D:
    print("{}: {} - {}".format(d,amounts[d],predictions[d]))
  print(grr.p)
  print(grr.q)

if not SKIP_SECOND:
  print("\n\n"+"-"*10+"Starting Second Experiment")
  amounts = {}
  for d in D: amounts[d]=AMOUNT
  print(f"Amount of each element is {AMOUNT}")
  print(f"Size of Domain is {len(D)}")
  print(f"Original Epsillon is {EPSILON}")
  estimates = []
  for y_selected in tqdm(D): #INEFFICIENT TODO DO THE SAME AS THIRD PART
    #print(f"Selected y value is {y_selected}")
    v_values ={}
    for d in D: v_values[d]=0
    for d in D:
      for _ in range(amounts[d]):
        if grr.f(d)==y_selected:
          v_values[d]+=1

    #print("Results of Experiment:")
    #for d in D:
    #  print(f"{v_values[d]} v values were mapped to {y_selected}")
    #print("Analyzing Probs...")
    min_val = np.array(list(v_values.values())).min()
    max_val = np.array(list(v_values.values())).max()
    #print(f"MAX:{max_val}")
    #print(f"MIN:{min_val}")
    estimate = np.log(max_val*1.0/min_val)
    estimates.append(estimate)
    #print(f"EPSILON ESTIMATE: {estimate}")
  print(f"Final Epsilon Estimate: {np.array(estimates).max()}")

if not SKIP_THIRD:
  print("\n\n"+"-"*10+"Starting Third Experiment")
  amounts = {}
  for d in D: amounts[d]=AMOUNT
  print(f"Amount of each element is {AMOUNT}")
  print(f"Size of Domain is {len(D)}")
  print(f"Original Epsillon is {EPSILON}")
  all_v_values ={}
  p_values = []
  for y in D:
    all_v_values[y] ={}
    for d in D:
      all_v_values[y][d]=0
  for d in tqdm(D):
    for _ in range(amounts[d]):
      y = grr.f(d)
      all_v_values[y][d]+=1
  for y_selected in tqdm(D):
    v_values = all_v_values[y_selected]
    for v1 in D:
      for v2 in D[D.index(v1)+1:]:
        val_max = max(v_values[v1],v_values[v2])
        val_min = min(v_values[v1],v_values[v2])
    #print("Results of Experiment:")
    #for d in D:
    #  print(f"{v_values[d]} v values were mapped to {y_selected}")
    #print("Analyzing Probs...")
    #min_val = np.array(list(v_values.values())).min()
    #max_val = np.array(list(v_values.values())).max()
    #print(f"MAX:{max_val}")
    #print(f"MIN:{min_val}")
    #estimate = np.log(max_val*1.0/min_val)
    #estimates.append(estimate)
    #print(f"EPSILON ESTIMATE: {estimate}")
  #print(f"Final Epsilon Estimate: {np.array(estimates).max()}")

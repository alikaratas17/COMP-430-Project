from LDP_Algorithms import GRR
from tqdm import tqdm
import numpy as np



def estimateEpsilonNonVectorized(algo,initial_amount,incremental_amount=None,sample_more_num=None):
  D = algo.getD()
  amounts = {}
  for d in D: amounts[d]=initial_amount
  all_v_values ={}
  for y in D:
    all_v_values[y] ={}
    for d in D:
      all_v_values[y][d]=0
  for d in D:
    for _ in range(amounts[d]):
      y = algo.f(d)
      all_v_values[y][d]+=1
  def getEstimates():
    estimates = []
    for y_selected in D:
      v_values = all_v_values[y_selected]
      min_v = D[0]
      max_v = D[0]
      min_val = v_values[min_v]*1.0/amounts[min_v]
      max_val = v_values[max_v]*1.0/amounts[max_v]
      for v in v_values.keys():
        current_val = v_values[v]*1.0/amounts[v]
        if current_val > max_val:
          max_v = v
          max_val = current_val
        if current_val < min_val:
          min_v = v
          min_val = current_val
      estimates.append((max_v,min_v,max_val,min_val))
    return estimates
  estimates = getEstimates()
  def find_max_estimate():
    max_estimate = None
    v_vals = None
    for max_v,min_v,max_val,min_val in estimates:
      current_estimate = np.log((max_val * 1.0)/ min_val)
      if max_estimate is None or max_estimate < current_estimate:
        max_estimate = current_estimate
        v_vals = min_v,max_v
    return max_estimate,v_vals
  max_estimate,v_vals = find_max_estimate()
  #print(f"Initial Estimate for epsilon is {max_estimate}")
  #print(v_vals)
  #print(all_v_values[v_vals[-1]])
  if sample_more_num is None or incremental_amount is None:
    return max_estimate
  def sample_more():
    for v in D:
      for _ in range(incremental_amount):
        y = algo.f(v)
        all_v_values[y][v]+=1
    amounts[v_vals[0]]+=incremental_amount
    amounts[v_vals[1]]+=incremental_amount
  for j in range(sample_more_num):
    sample_more()
    estimates = getEstimates()
    max_estimate,v_vals = find_max_estimate()
    #print(f"Estimate #{j+2} is {max_estimate}")
  return max_estimate

N = 10000
N_str = str(N)
if len(N_str)>3:
  N_str = N_str[:-3]+","+N_str[-3:]
print("Number of samples for each v:",N_str)
for epsilon in [0.25, 0.5, 0.75, 0.9, 1.0, 1.25, 1.5,2.0,2.5]:
  grr = GRR.GRR(epsilon,10)
  estim = estimateEpsilonNonVectorized(grr,N)
  print(f"Actual epsilon: {epsilon}, Esimate: {estim}")

''' 
    #min_val = np.array(list(v_values.values())).min()
    #max_val = np.array(list(v_values.values())).max()
    

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
'''










'''
EPSILON = 1.0
MIN_AMOUNT = 10000
MAX_AMOUNT = 20000
LEN_D = 10
SKIP_FIRST = True
SKIP_THIRD = True
AMOUNT = 10000
'''
'''



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
'''
from LDP_Algorithms import GRR
from tqdm import tqdm
import numpy as np



def estimateEpsilonNonVectorized(algo,N):
  D = algo.getD()
  amounts = {}
  for d in D: amounts[d]=N
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
  return max_estimate

def estimateEpsilonVectorized(algo,N):
  Y = [[]]
  D = algo.getD()
  for d in D:
    new_Y = []
    for y in Y:
      new_Y.append(y+[0])
      new_Y.append(y+[1])
    Y = new_Y
  Y = [tuple(y) for y in Y]
  D = algo.getD()

  amounts = {}
  for d in D: amounts[d]=N
  
  all_y_values ={}
  for y in Y:
    all_y_values[y] ={}
    for d in D:
      all_y_values[y][d]=0

  for d in D:
    for _ in range(amounts[d]):
      y = algo.f(d)
      all_y_values[tuple(y)][d]+=1

  def getEstimates():
    estimates = []
    for y_selected in Y:
      v_values = all_y_values[y_selected]
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
  return max_estimate

if __name__=='__main__':

  N = 10000
  N_str = str(N)
  if len(N_str)>3:
    N_str = N_str[:-3]+","+N_str[-3:]
  print("Number of samples for each v:",N_str)
  for epsilon in [0.25, 0.5, 0.75, 0.9, 1.0, 1.25, 1.5,2.0,2.5]:
    grr = GRR.GRR(epsilon,10)
    estim = estimateEpsilonNonVectorized(grr,N)
    print(f"Actual epsilon: {epsilon}, Esimate: {estim}")

from .LDP_Base import LDP_Base
import numpy as np

class RR(LDP_Base):

  def __init__(self,epsilon=None):
    self.epsilon = epsilon
    self.D = [0,1]

# RR algorithm
# v is the real response value
  def f(self,v):
    if np.random.uniform()>=0.5:
      return v
    if np.random.uniform()>=0.5:
      return self.D[0]
    return self.D[1]

# calculate c(n_v) (unbiased estimator)
  def g(self, y_values:dict)->dict:
    results = {}
    item0 = self.D[0]
    item1 = self.D[1]
    total = y_values[item0]+y_values[item1]
    results[item0] = (y_values[item0] - 0.25 * total)/ 0.5
    results[item1] = (y_values[item1] - 0.25 * total)/ 0.5
    return results

  def getD(self)->list:
    return self.D
  def isVectorized(self)->bool:
    return False


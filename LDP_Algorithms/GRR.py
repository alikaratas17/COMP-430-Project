from .LDP_Base import LDP_Base
import numpy as np

class GRR(LDP_Base):

  def __init__(self,epsilon,max_D=50):
    self.is_vectorized = False
    self.epsilon = epsilon
    self.D = list(range(max_D))
    self.p = np.exp(self.epsilon)/(np.exp(self.epsilon)+len(self.D)-1)
    self.q = (1 - self.p)/(len(self.D)-1)

  def f(self,v):
    probs = [self.q for _ in self.D]
    probs[self.D.index(v)] = self.p
    return np.random.choice(self.D,p=probs)

  def g(self, y_values:dict,total)->dict:
    results = {}
    total = np.array(list(y_values.values())).sum()
    for item in self.D:
      results[item] = (y_values[item] - total*self.q)/(self.p-self.q)
    return results
  def getD(self)->list:
    return self.D
  def isVectorized(self)->bool:
    return False

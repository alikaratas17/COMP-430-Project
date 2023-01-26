from .LDP_Base import LDP_Base
import numpy as np


class SimpleRAPPOR(LDP_Base):

    def __init__(self, epsilon, max_D=50):
        self.epsilon = epsilon
        self.D = list(range(max_D))
        self.p = np.exp(self.epsilon/2)/(np.exp(self.epsilon/2)+1)
        self.q = 1/(np.exp(self.epsilon/2)+1)

    def f(self, v):
        vect = np.array([0 for _ in self.D])
        vect[v] = 1
        flip = np.random.uniform(size=len(self.D)) < self.q
        flipped = (1-vect)
        keep = np.random.uniform(size=len(self.D)) < self.p
        return vect * (keep) + flipped * flip

    def g(self, y_values: dict,total) -> dict:
        results = {}
        #total = np.array(list(y_values.values())).sum()
        for item in self.D:
            results[item] = (y_values[item] - total*self.q)/(self.p-self.q)
        return results

    def getD(self) -> list:
        return self.D

    def isVectorized(self) -> bool:
        return True

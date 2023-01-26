from .LDP_Base import LDP_Base
import numpy as np


class OUE(LDP_Base):

    def __init__(self, epsilon, max_D=10):
        self.epsilon = epsilon
        self.D = list(range(max_D))

    def f(self, v):
        vect = 1*(np.random.uniform(size=len(self.D))
                  < (1/(np.exp(self.epsilon)+1)))
        if np.random.uniform() < 0.5:
            vect[v] = 1
        else:
            vect[v] = 0
        return vect

    def g(self, y_values: dict,total) -> dict:
        results = {}
        #total = np.array(list(y_values.values())).sum()
        for item in self.D:
            results[item] = 2.0*((np.exp(self.epsilon)+1) *
                                 y_values[item] - total)/(np.exp(self.epsilon)-1)
        return results

    def getD(self) -> list:
        return self.D

    def isVectorized(self) -> bool:
        return True

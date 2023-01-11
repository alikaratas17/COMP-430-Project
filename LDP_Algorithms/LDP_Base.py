from abc import ABC, abstractmethod

class LDP_Base(ABC):
  @abstractmethod
  def __init__(self,epsilon:float):
    pass
  @abstractmethod
  def f(self,v):
    pass
  @abstractmethod
  def g(self, y_values)->dict:
    pass
  @abstractmethod
  def getD(self)->list:
    pass
  @abstractmethod
  def isVectorized(self)->bool:
    pass

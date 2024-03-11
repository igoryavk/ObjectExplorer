from abc import ABC
from abc import abstractmethod

class Explorer(ABC):
    @abstractmethod
    def createDOM(self,path:str):
        pass
    @abstractmethod
    def explore(self,show:list):
        pass
    @abstractmethod
    def exploreList(self):
        pass


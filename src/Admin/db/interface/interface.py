from abc import (abstractmethod,ABC)



class Interface(ABC):     
    @abstractmethod
    def Conect(self):
        raise "You have implement this func!"

    @abstractmethod
    def Create_table(self):
        raise "You have implement this func!"

    @abstractmethod
    def Desconect(self):
        raise "You have implement this func!"

    @abstractmethod
    def Insert(self):
        raise "You have implement this func!"

    @abstractmethod
    def Delete(self):
        raise "You have implement this func!"    

    @abstractmethod
    def Select(self):
        raise "You have implement this func!"        

    @abstractmethod
    def Update(self):
        raise "You have implement this func!"            

     
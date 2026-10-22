from abc import ABC , abstractmethod

class NaveEspacial (ABC):
    modelo:str
    def __init__(self,modelo:str):
        self.modelo = modelo

    @abstractmethod
    def Despegar(self):
        pass

class NaveCapsula(NaveEspacial):

    def __init__(self, modelo:str):
        super().__init__(modelo)

    def Despegar(self):
        print(self.modelo,"Despegar con metores de capsula corp")

class NaveSaiyayin(NaveEspacial):
    def __init__(self, modelo:str):
        super().__init__(modelo)
    def Despegar(self):
        print(self.modelo,"Despegar inmediatamente")

naveBulma =NaveCapsula("Nave de bulma")
naveVegeta=NaveSaiyayin("Capsula saiyayin")
naveBulma.Despegar()
naveVegeta.Despegar()
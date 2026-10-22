class Guerrero:
    nombre:str
    def __init__(self,nombre:str):
        self.nombre=nombre
    def presentarse (self):
        print("mi poderoso nombre es :" ,self.nombre)


class Androide:
    nombre: str
    energia:int

    def __init__(self,nombre:str,energia:int):
        self.nombre = nombre
        self.energia = energia

    def mostrarEnergia(self):
        print("androide: ", self.nombre)
        print("energia: ", self.energia)

class AndroideRecargable(Androide):
    def __init__(self, nombre: str,energia:int):
        super().__init__(nombre,energia)

    def recarga(self,cantidad:int):
        if cantidad >0:
            self.energia += cantidad

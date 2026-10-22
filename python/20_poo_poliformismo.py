class Guerrero:
    nombre:str
    poderInicial:int
    horas:int
    def __init__(self,nombre:str, poder_inicia:int, horas: int):
        self.nombre=nombre
        self.poderInicial=poder_inicia
        self.horas=horas

    def Atacar(self):
        print(f"{self.nombre} Realiza Ataque")

    def calcularPoder(self):
        return self.poderInicial

class Goku(Guerrero):
    def __init__(self,nombre:str):
        super().__init__(nombre)
    def Atacar(self):
        print(self.nombre, "Utiliza Kamehameha")
    def calcularPoder(self):
        return self.poderInicial + self.horas*100

class Vegeta(Guerrero):
    def __init__(self, nombre:str):
        super().__init__(nombre)

class Guerrero:
    nombre: str
    def __init__(self, nombre: str):
        self.nombre = nombre

    def presentarse(self):
        print("Mi poderoso nombre es: ", self.nombre)

class saiyajin(Guerrero):
    def __init__(self, nombre: str):
        super().__init__(nombre)
    
    def transformarse(self):
        print(self.nombre, "Se transforma en super saiyajin")

Goku = saiyajin("Goku")
Goku.presentarse()
Goku.transformarse()

class Androide:
    nombre: str
    energia: int

    def __init__(self, nombre: str, energia: int):
        self.nombre = nombre
        self.energia = energia
    
    def mostrarEnergia(self):
        print("Androide: ", self.nombre)
        print("Energia: ", self.energia)

class AndroideRecargable(Androide):
    def __init__(self, nombre: str, energia: int):
        super().__init__(nombre, energia)
    
    def recargar(self, cantidad: int):
        if cantidad > 0:
            self.energia += cantidad
            
androide17 = AndroideRecargable("N17", 600)
print("|--- ANTES DE RECARGAR ---|")
androide17.mostrarEnergia()
print("|--- DESPUES DE RECARGAR ---|")
androide17.recargar(100)
androide17.mostrarEnergia()
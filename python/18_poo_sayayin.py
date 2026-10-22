from poo_herencia import Guerrero


class saiyajin(Guerrero):
    def __init__(self, nombre: str):
        super().__init__(nombre)
    
    def transformarse(Self):
        print(Self.nombre, "Se transforma en super saiyajin")

Goku = saiyajin("Goku")
Goku.presentarse()
Goku.transformarse()
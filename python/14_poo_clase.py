class guerrero:
    nombre: str
    poder: int
    def __init__(self, nombre:str, poder:int):
        self.nombre = nombre
        self.poder = poder

    def saludar(self):
        print("hola soy: ", self.nombre)
        print("Mi poder es de: ", self.poder)

    def entrenar(self, aumento):
        aumento=200
        self.poder+=aumento

    def atacar(self, cantidad):
        daño=self.poder*cantidad
        print("Guerrero: ", self.nombre)
        print("Daño causado: ", daño)

goku=guerrero("Goku", 9000)
goku.saludar()

goku.entrenar(100)
print("Poder de goku es: ", goku.nombre)

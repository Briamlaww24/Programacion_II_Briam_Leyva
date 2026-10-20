
class AlmacenSemillas:
    __cantidad: int

    def __init__(self, cantidad: int):
        self.__cantidad = cantidad

    def get_cantidad(self):
        return self.__cantidad

    def set_cantidad(self, cantidad: int):
        if cantidad >= 0:
            self.__cantidad = cantidad
        else:
            print("La cantidad no puede ser negativa")

    def entregar_semillas(self, cantidad: int, persona: str):
        if cantidad <= self.__cantidad:
            self.__cantidad -= cantidad
            print(f"Se han entregado {cantidad} semillas a {persona}. Quedan {self.__cantidad} semillas en el almacén")
        else:
            print(f"No hay suficientes semillas para entregar esa cantidad a {persona}")

almacen = AlmacenSemillas(10)
almacen.entregar_semillas(3, "Goku")
almacen.entregar_semillas(9, "Yajirobe")
print("Cantidad de semillas en el almacen:", almacen.get_cantidad())    

class RadarDragon:
    region1: int
    region2: int
    def __init__(self, region1:int, region2:int):
        self.region1 = region1
        self.region2 = region2

    def buscar_esferas(self):
        faltanRegion1 = 7 - self.region1
        print(f"Se han encontrado {self.region1} esferas, faltan {faltanRegion1}")
        faltanRegion2 = 7 - self.region2
        print(f"Se han encontrado {self.region2} esferas, faltan {faltanRegion2}")

bulma=RadarDragon(3, 2)
bulma.buscar_esferas()









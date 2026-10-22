Flota = [
    {
        "N1-001": {
        "Nombre": "Caza N-1",
        "Combustible": 80
        },
    },
    {
        "NR-002": {
        "Nombre": "Nave Real",
        "Combustible": 35
        }
    }
]

def crearNave(nave):
    Flota.append(nave)

def ActualizarNave(naveActualizada, index):
    Flota[index].update[naveActualizada]

def leerNave(index):
    return Flota.pop(index)

def borrarNave(index):
    return Flota.pop(index)

nuevaNave = {
    "Nr-003": {
        "Nombre": "Nave Real 2",
        "Combustible": 80
    },
}
crearNave(nuevaNave)
print(Flota)
print(Flota)

naveActualizada = {
    "NR-006": {
        "Nombre": "Nave real NR6", 
        "Combustible": 85
    }
}

ActualizarNave(naveActualizada, 2)
print(Flota)
print(leerNave(2))
print(borrarNave(2))
print(Flota)
# Funciones

def activarSistema():
    print("|-- sistema de naboo --|")
    print("sistema de Control Activado")

activarSistema()

#Funciones de parametros

def saludarJedi(nombre):
    print(f"que la fuerza te acopmañe: {nombre}")

saludarJedi("qui-go jim")
saludarJedi("obi-wan kenobi")

def mostrarNave(nombre,combustible):
    print(f"nave: {nombre}")
    print(f"cantidad combustible: {combustible}")

mostrarNave("Caza n-1", 80)

#Funciones que devulven datos o informacion
#Return

def calcularCombustible(inicial,consumo):
    restante =inicial - consumo
    return restante
Resultado = calcularCombustible(100,25)
print(f"Combustible: {Resultado}")
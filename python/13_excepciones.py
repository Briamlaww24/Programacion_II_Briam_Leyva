print("|--- CONTROL DE ENERGIA ---|")
energiaText= "Ochenta"
try:
    Energia = int("Mucho")
    print(Energia)
except ValueError:
    print("Error : Debe ser numerico")

print("Fin del sistema")

"""

ValueError
TypeError
keyError
IndexError
ZeroDivision

"""

def calcularEnergia(Total, Cantidad):
    try:
        Resultado = Total / Cantidad
        return Resultado
    except ZeroDivisionError as error:
        print("Error: division entre cero", error)
        return None
    except TypeError:
        print("Error: valores deben ser numericos")
        return None

print("Caso 1: ", calcularEnergia(100,4))
print("Caso 2: ", calcularEnergia(100/0))
print("Caso 3:", calcularEnergia(100, "Cautro"))

print("|--- DIAGNOSTICO R2-D2 ---|")
try:
    Energia = int(90)
    print("Energia ", Energia)
except ValueError:
    print("Error de lectura")
else:
    print("Diagnostico completado")
finally:
    print("Cerrando diagnostico")

def validarEnergia(Energia):
    if type(Energia) is not int:
        raise TypeError("La energia debe ser numero entero")
    if Energia < 0 or Energia > 100:
        raise ValueError("La energia debe estar entre 0 y 100")
    return Energia

try:
    Resultado = validarEnergia(150)
    print("Energia", Resultado)
except(TypeError, ValueError) as error:
    print("Error: ", error)
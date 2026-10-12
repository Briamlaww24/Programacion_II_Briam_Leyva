# Condicional if
# Simple

combustible = 5
if combustible >= 10:
    print("La nave puede despegar")

# Condicionales in - else
creditos = int(input("Ingrese la cantidad de creditos: "))
precioRespuesta = int(input("Ingrese el precio de la respuesta: "))
if creditos >= precioRespuesta:
    print("La nave puede despegar")
else:
    print("La nave no puede despegar")

# If anidado 
if creditos >= precioRespuesta:
    print("La nave puede despegar")
    if creditos > precioRespuesta:
        print("Le sobran creditos")
    else:
        print("Le faltan creditos")
else:
    print("La nave no puede despegar")      

# Condicionales elif
if creditos >= precioRespuesta:
    print("La nave puede despegar")
elif creditos == precioRespuesta:
    print("La nave puede despegar, pero no le sobran creditos")
else:
    print("La nave no puede despegar")  

tipoRepuesto = input("Ingrese el tipo de repuesto (motor, ala o escudo): ")
if tipoRepuesto == "motor" and creditos >= precioRespuesta and tipoRepuesto == "motor":
    print("puede comprar el repuesto")
elif tipoRepuesto == "ala" and creditos >= precioRespuesta and tipoRepuesto == "ala":
    print("puede comprar el repuesto")
elif tipoRepuesto == "escudo" and creditos >= precioRespuesta and tipoRepuesto == "escudo":
    print("puede comprar el repuesto")
else:
    print("no puede comprar el repuesto")  

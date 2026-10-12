# Ejercicio 1

print("Escriba el peso de su paquete en kilogramos: ")
pesoDecimales = float(input("-: "))
print("Escriba la zona a la que quiere enviar su paquete (1, 2 o 3):")
print("1.(america): $5.0 por kilo")
print("2.(europa): $7.5 por kilo")
print("3.(resto del mundo): $10.0 por kilo")
print("Escriba el numero de la zona: ")
zona = int(input("-: "))

if zona == 1:
    costoEnvio = precioEnvio = pesoDecimales * 5.0
    print("El costo de envio es: $", costoEnvio)
elif zona == 2:
    costoEnvio = precioEnvio = pesoDecimales * 7.5
    print("El costo de envio es: $", costoEnvio)   
elif zona == 3:
    costoEnvio = precioEnvio = pesoDecimales * 10.0
    print("El costo de envio es: $", costoEnvio)
else:
    print("Zona no válida. Por favor, seleccione una zona válida (1, 2 o 3).") 
# Operadores
"""
operadores aritméticos
+ suma
- resta
* multiplicación
/ división
// división entera
% módulo
** potencia
"""

valor1 = 10
valor2 = 3
resultado = valor1 + valor2
resta = valor1 - valor2
multiplicacion = valor1 * valor2
division = valor1 / valor2
division_entera = valor1 // valor2
modulo = valor1 % valor2
potencia = valor1 ** valor2

print("Suma:", resultado)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("División entera:", division_entera)
print("Módulo:", modulo)
print("Potencia:", potencia)

print("tabla de multiplicar del 5")
print("5 x 1 =", 5 * 1)
print("5 x 2 =", 5 * 2)
print("5 x 3 =", 5 * 3) 
print("5 x 4 =", 5 * 4)
print("5 x 5 =", 5 * 5)
print("5 x 6 =", 5 * 6)
print("5 x 7 =", 5 * 7)
print("5 x 8 =", 5 * 8)
print("5 x 9 =", 5 * 9)
print("5 x 10 =", 5 * 10)

"""
operadores de comparación
== igual a
!= diferente de
> mayor que           
< menor que
>= mayor o igual que
<= menor o igual que
"""
print("area del tringulo con base 5 y altura 10", (5 * 10) / 2)
velocidadAnakin = 950
velocidadLuke = 1000
print("¿Anakin es más rápido que Luke?", velocidadAnakin > velocidadLuke)
print("¿Anakin es más lento que Luke?", velocidadAnakin < velocidadLuke)
print("¿Anakin es igual de rápido que Luke?", velocidadAnakin == velocidadLuke)
print("¿Anakin es diferente de Luke?", velocidadAnakin != velocidadLuke)
print("¿Anakin es más rápido o igual que Luke?", velocidadAnakin >= velocidadLuke)
print("¿Anakin es más lento o igual que Luke?", velocidadAnakin <= velocidadLuke)

resultado = velocidadAnakin > velocidadLuke
print("Resultado de la comparación:", resultado)
print("Tipo de resultado:", type(resultado))

# Operadores lógicos

"""
and (y)
or (o)
not (no)
"""

motorEncendido = True
naveEnMovimiento = False

print("¿La nave puede despegar?", motorEncendido and naveEnMovimiento)
print("¿La nave puede despegar?", motorEncendido or naveEnMovimiento)
print("¿La nave puede despegar?", not motorEncendido)

cantidadMotores = 2
cantidadAlas = 4
combustible= 50

print("¿La nave puede despegar?")
print(cantidadMotores >= 2 and cantidadAlas >= 4 and combustible > 0)

# Operadores de asignación
"""
= asignación
+= suma y asigna
-= resta y asigna
*= multiplica y asigna
/= divide y asigna
//= divide entera y asigna
%= módulo y asigna
**= potencia y asigna
"""
velocidad = 100
print("velocidad inicial", velocidad)
velocidad += 50
print("velocidad después de acelerar", velocidad)
velocidad -= 30
print("velocidad después de frenar", velocidad)
velocidad **= 2
print("velocidad después de potenciar", velocidad)
velocidad //= 3
print("velocidad después de dividir entera", velocidad)
velocidad %= 7
print("velocidad después de módulo", velocidad)
velocidad *= 2
print("velocidad después de multiplicar", velocidad)
velocidad /= 4
print("velocidad después de dividir", velocidad)

# Precencia de operadores
"""
1. ()
2. ** (potencia)
3. * / // % (multiplicación, división, división entera, módulo)
4. + - suma, resta
"""
resultado = 10 + 5 * 2
print("Resultado de 10 + 5 * 2:", resultado)
resultado = (10 + 5) * 2
print("Resultado de (10 + 5) * 2:", resultado)
resultado = 10 + 5 ** 2
print("Resultado de 10 + 5 ** 2:", resultado)

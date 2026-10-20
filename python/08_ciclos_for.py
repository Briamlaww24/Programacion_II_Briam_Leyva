# Ciclos For

naves = [
    "Casa N-1",
    "Nave Real de Naboo",
    "Transporte",
]

for i in naves:
    print(f"Inspeccionando: {i}")

print("Inspeccion Realizada")

rondas = range(1, 6)
print(f"Tipo de la variable ronda: {type(rondas)}")
for i in rondas:
    print("Ronda de Vigilancia: ", i)
    print("Tipo de dato ronda: ", type(i))


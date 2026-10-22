
# Control de flota de naboo

Naves = [
    {
        "nombre": "caza n-1",
        "combustible": 10,
        "droide": ["r2-d2"]
   },
   {
        "nombre": "trasportador",
        "combustible": 10,
        "droide": ["r2-n3"]
   },
      {
        "nombre": "real caza",
        "combustible": 5,
        "droide": ["r2-d2", "r2-n3"]
   }
]

navesListas=0
navesRecarga=0
totalDroides=0
totalCiclos=0

for Numero,Nave in enumerate(Naves,start=1):
    print(f"-nave : {Numero}-{Nave}")
    if Nave ["combustible"] >= 50:
        print(f"estado inicial:LISTA")
        navesListas += 1
    else:
        print(f"estado inicial: RECARGAR")
        navesRecarga += 1
        Ciclo=0
        while Nave["combustible"] <= 50:
            Ciclo +=1
            Nave["combustible"] += 10
        totalCiclos += Ciclo
        print("recarga completa")
        print("estado final: LISTA")
    totalDroides+=len(Nave["droide"])
    for droide in Nave ["droide"]:
        print(f"droide: {droide}") 
print("------------------------------------")           
print("Resumen")
print("------------------------------------")
print(f"Total Naves: {len(Naves)}")
print(f"Naves Listas Inicialmente: {navesListas}")
print(f"Naves Recargadas: {navesRecarga}")
print(f"Total Droides: {totalDroides}")
print(f"Total Ciclos: {totalCiclos}")
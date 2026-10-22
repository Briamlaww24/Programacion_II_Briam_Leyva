Droides =[
    {
        "Codigo":"B1-001",
        "Modelo": "B1",
        "Energia": 100,
        "Activo": True
    },
    {
        "Codigo":"B1-002",
        "Modelo": "B1",
        "Energia": 30,
        "Activo": False
    },
    {
        "Codigo":"B1-003",
        "Modelo": "B1",
        "Energia": 70,
        "Activo": True
    }
]
cantidadDroides =len(Droides)
print(cantidadDroides)
nuevoDroide={
        "Codigo":"B1-004",
        "Modelo": "B1",
        "Energia": 15,
        "Activo": False
}

#CRUD
#CREATE

Droides.append(nuevoDroide)
print(len(Droides))
print(Droides)

#READ

Droide = Droides[0]
print(f"codigo: {Droide["codigo"]}")
print(f"modelo: {Droide["modelo"]}")
print(f"energia: {Droide["energia"]}")
print(f"activo: {Droide["activo"]}")

#UPDATE

Droide = Droides[2]
Droide["codigo"]="DRO-002"
Droide["energia"]=85
Droide["activo"]=False
print(f"droides: {Droides}")

#DELET

eliminado = Droides.pop(2)
print(f"droide : {Droides}")
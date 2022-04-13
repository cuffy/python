diccionario = dict()

nombre = input("Introduce tu nombre: ")

asignaturas = []
for i in range(3):
    asignaturas.append(input("Introduce una asignatura: "))

diccionario["name"] = nombre
diccionario["asignaturas"] = asignaturas

print(diccionario)

print("Tu nombre es:", diccionario["name"])
print("Las asignaturas son:", ", ".join(diccionario["asignaturas"]))

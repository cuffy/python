import student

n = int(input("Introduce cuantos estudiantes tienes: "))
lista_estudiantes = []

for i in range(n):
    name = input("Introduce el nombre del estudiante: ")
    age = input("Introduce la edad del estudiante: ")
    where_from = input("Introduce que nacionalidad es:  ")

    lista_estudiantes.append(student.Student(name, age, where_from))

print("Las nacionalidades són: ", end="")
for e in lista_estudiantes:
    print(e.where_from, end=", ")

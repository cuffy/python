from os import mkdir
from os.path import exists


"Si la carpeta no existe se crea"
if not exists("./data"):
    mkdir("./data")

numero = None

while numero is None:
    try:
        numero = int(input("Introduce el número entre 1 y 10: "))
        if numero < 1 or numero > 10:
            raise TypeError("Introduce un número entre el 1 y 10 incluidos.")
    except ValueError:
        numero = None
        print("Por favor introduce un número")

lines = []
for i in range(1, 11):
    lines.append("{} x {} = {}\n".format(i, numero, i * numero))

with open("data/tabla-{}.txt".format(numero), "w") as f:
    f.writelines(lines)

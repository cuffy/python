animals = {"cerdo": "oink", "rana": "croac", "vaca": "muu"}

for a in ["cerdo", "vaca"]:
    ruido = animals[a]
    print("{} tiene el gruñido {}".format(a, ruido))

if "gato" not in animals:
    print("No existe el gato")

animals.update({"gato": "miau"})

print("El ruido del gato es", animals["gato"])

animals["perro"] = "guau"

print("El ruido del perro es", animals["perro"])

if "perro" in animals:
    del animals["perro"]

print(animals)

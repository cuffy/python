edad = input("Tu edad: ")

try:
    edad = int(edad)
    if edad > 18:
        print("Bienvenido!")
    else:
        raise Exception("Eres menor de edad.")
except ValueError:
    print("ValueError. Número no válido")
except Exception as e:
    print(e)
finally:
    print("Final del programa")


char = input("Introduce un carácter: ")

# Pasamos el carácter a minusculas con la función lower
char = char.lower()

print()

if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
    print("Es una vocal")
else:
    print("No es una vocal")

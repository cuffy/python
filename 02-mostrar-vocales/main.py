text = input("Introduce un texto: ")

n = 0
vocales = ""

for c in text:
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        n += 1
        vocales += c + " "

print(vocales, "Total de vocales:" + str(n))

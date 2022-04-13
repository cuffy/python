import random

numeros = []
random.seed(1)

for i in range(10):
    n = random.randint(1, 20)
    numeros.append(n)

numeros.sort()

min = numeros[0] 
max = numeros[-1]

print(numeros, min, max)
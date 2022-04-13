
array_ordenar = [32, 49, 37, 45, 59, 6, 41, 48, 65, 44, 12, 3, 74, 45, 83]

n = len(array_ordenar)

print(array_ordenar)
for i in range(1, n-1):
    for j in range(n-i-1):
        if array_ordenar[j] > array_ordenar[j+1]:
            aux = array_ordenar[j]
            array_ordenar[j] = array_ordenar[j+1]
            array_ordenar[j+1] = aux
print(array_ordenar)



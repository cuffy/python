
array = []

# Se rellena el array
for i in range(10):
    array.append(i)

print("El array es:", array)

min = None
max = None

# Se calcula el min y max
for a in array:
    if min is None:
        min = a
    elif a < min:
        min = a

    if max is None:
        max = a
    elif a> max:
        max = a
print("El minimo es:", min)
print("El maximo es:", max)

i = 0
add = 0
# Se calcula la media
while i < 10:
    add += array[i]
    i += 1

print("La media es:", add/10)

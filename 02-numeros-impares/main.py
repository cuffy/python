num = int(input("Introduce un numero: "))

if num > 1:
    for i in range(1, num+1):
        if i % 2 != 0:
            print(i, end=" ")
else:
    print("El número tiene que ser > 1")

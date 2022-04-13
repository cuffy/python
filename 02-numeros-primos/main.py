
numeros_primos = []

#Se realiza un for porque se sabe quantos bucles hay que hacer, en principio 3 números primos
for i in range(3):
    #El segundo bucle es while porque minimo que se tiene que preguntar es una vez para conseguir un numero primo
    while True:
        number = int(input("Introduce un número primo: "))
        if number == 1 or number == 2 or number == 3:
            numeros_primos.append(number)
            break
        else:
            n = number - 1
            es_primo = True
            while n > 1:
                if number % n == 0:
                    es_primo = False
                    break
                n -= 1
            if es_primo:
                numeros_primos.append(number)
                break

print(numeros_primos)

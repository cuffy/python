def show_menu():
    print("=====[ MENU ]=====")
    print("   1. Sumar")
    print("   2. Restar")
    print("   3. Multiplicar")
    print("   4. Dividir")
    print("   5. Factorial")
    print()
    print("   6. Salir")

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def division(n1, n2):
    result = None
    if n2 != 0:
        result = n1 / n2
    return result

def factorial(n1):
    if n1 == 1:
        return 1
    else:
        return n1 * factorial(n1-1)


while True:
    show_menu()
    option = int(input("Que operacion quieres realizar: "))
    if option == 1:
        n1 = int(input("Introduce un numero: "))
        n2 = int(input("Introduce otro numero: "))
        print("El resultado de la suma es:", add(n1, n2))
    elif option == 2:
        n1 = int(input("Introduce un numero: "))
        n2 = int(input("Introduce otro numero: "))
        print("El resultado de la resta es:", substract(n1, n2))
    elif option == 3:
        n1 = int(input("Introduce un numero: "))
        n2 = int(input("Introduce otro numero: "))
        print("El resultado de la multiplicación es:", multiply(n1, n2))
    elif option == 4:
        n1 = int(input("Introduce un numero: "))
        n2 = int(input("Introduce otro numero: "))
        result = division(n1, n2)
        if result is None:
            print("No se puede dividir por cero.")
        else:
            print("El resultado de la división es:", result)
    elif option == 5:
        while True:
            n1 = int(input("Introduce un numero(1 y 15): "))
            if n1 > 1 or n1 <= 15:
                break
            else:
                print("El numero tiene que ser mayor que 1 y menor que 15")
        print("El resultado del factorial es:", factorial(n1))
    elif option == 6:
        break

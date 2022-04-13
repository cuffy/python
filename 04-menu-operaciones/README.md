# Menu Operaciones
## Enunciado
Realizar el programa que sea capaz de:
1. Mostrar un menú con 6 opciones (1.‐ Sumar, 2.‐ Restar, 3.‐ Multiplicar, 4.‐ Dividir, 5.‐ Factorial, 6.- Salir) y pregunte al usuario qué desea hacer.
2. Mientras el usuario no seleccione la opción 6, seguiremos mostrando el menú y
operando.
3. En cualquiera de las otras 4 opciones solicitaremos al usuario (cada vez) dos números y
calcularemos su correspondiente resultado, mostrándolo por pantalla. En el caso de calcular el factorial, sólo solicitaremos un número, que deberá ser natural mayor de 1 y menor de 15.
4. Recordad que no se puede dividir por 0.
5. Cada una de las 5 operaciones, se realizarán en una función.
6. El cálculo del factorial se realizará mediante recursividad


**Se considera que el usuario introducirá únicamente numéricos.**

### Pistas
1. Usad un bucle while para el menú.
2. Usad una acción que muestre el menú, tendréis el código más limpio.
3. Anidad bucles si es necesario.
4. Podéis usar if/else.


### Test data
#### Input data
1. Se introduce los números: `3 9` para realizar una suma
2. Se introduce los números: `4 2` para realizar una division
3. Se introduce los números: `4 0` para realizar una division
4. Se introduce el número: `4` para realizar el factorial
5. Se introduce al menú el número: `6`

#### Output
1. El resultado es el siguiente:
```
El resultado de la suma es: 12
```
2. El resultado es el siguiente:
```
El resultado de la división es: 2.0
```
3. El resultado es el siguiente:
```
No se puede dividir por zero.
```
4. El resultado es el siguiente:
```
El resultado del factorial es: 24
```
5. El programa finaliza correctamente

### Solución
El contenido del código se encuentra en el fichero: **main.py**
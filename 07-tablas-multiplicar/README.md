# Tablas de multiplicar
## Enunciado
Realizar el programa que sea capaz de leer por pantalla un número entero entre 1 y 10 y guarde en un fichero con el 
nombre tabla-n.txt en el directorio data/

Mostrar una excepción de TypeError si el número no esta entre el rango del enunciado.

### Pistas
NA

### Test data
#### Input data
1. Se introduce los números: `3`
2. Se introduce los números: `6`
3. Se introduce los números: `20`

#### Output
1. El resultado es el siguiente:
```
data/
    tabla-3.txt
    tabla-6.txt
```
2. El resultado es el siguiente:
```
data/
    tabla-6.txt
```

3. El resultado es el siguiente:
```
Traceback (most recent call last):
  File "D:/Projectes/python-exercises/07-tablas-multiplicar/main.py", line 15, in <module>
    raise TypeError("Introduce un número entre el 1 y 10 incluidos.")
TypeError: Introduce un número entre el 1 y 10 incluidos.
```

### Solución
El contenido del código se encuentra en el fichero: **main.py**

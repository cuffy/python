# Validación del email
## Enunciado
Realizar el programa que sea capaz de leer de una lista de emails y mostrar por pantalla si la 
dirección es válida o no, utilizar una función para este caso.

Una dirección se considerará válida:
1. Si contiene el símbolo "@".
2. Tiene una longitud mayor que 2.

### Pistas
Declara una función con:
1. Un parametro de entrada
2. Devolver el resultado un booleano
3. Utilizar la función [strip()](https://docs.python.org/3/library/stdtypes.html#str.strip) para quitar los espacios.


### Test data
#### Input data
La variable de emails es:`["hellopython","hello@python.es","   "," @"]`

#### Output
El resultado es el siguiente:
```
False True False False 
```

### Solución
El contenido del código se encuentra en el fichero: **main.py**
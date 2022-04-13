# Operación aritmética: División
## Enunciado
Realizar el programa que sea capaz mediante una función devolver el resultado de la división pasándole como parámetro dos números:
```python
divide(2, 1)
divide(2, 0)
divide("2", "1")
```

### Pistas
* Controlar la excepción: ZeroDivisionError.


### Test data
#### Input data
Se realiza la prueba del enunciado.

#### Output
El resultado es el siguiente:
```
result is 2.0
executing finally clause

division by zero!
executing finally clause

executing finally clause
Traceback (most recent call last):
  File "D:/Projectes/python-exercises/05-operacion-division/main.py", line 15, in <module>
    divide("2", "1")
  File "D:/Projectes/python-exercises/05-operacion-division/main.py", line 3, in divide
    result = x / y
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```

### Solución
El contenido del código se encuentra en el fichero: **main.py**

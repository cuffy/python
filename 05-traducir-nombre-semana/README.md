# Traducir nombre semana
## Enunciado
Realizar el programa que sea capaz mediante una función devolver el dia de la semana en catalan:
````python
def get_translate_catalan(english_day):
    catalan = None
    dict_week = {"monday": "Dilluns",
                 "tuesday": "Dimarts",
                 "wednesday": "Dimecres",
                 "thursday": "Dijous",
                 "friday": "Divendres",
                 "saturday": "Dissabte",
                 "sunday": "Diumenge"}
    ## define code
    return catalan

## Define code
print(get_translate_catalan(None))
print(get_translate_catalan("monday"))
print(get_translate_catalan("Python"))
print(get_translate_catalan("Sunday"))
````

### Pistas
* Controlar el parámetro de entrada.
* Controlar la palabra en el diccionario y si no está lanzar una excepción con raise.


### Test data
#### Input data
N.A

#### Output
1. El resultado de la ejecución del script es:
```
None
Dilluns
El texto no es un día de la semana.
Diumenge
```

### Solución
El contenido del código se encuentra en el fichero: **main.py**

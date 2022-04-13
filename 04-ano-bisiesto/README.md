# Año bisiesto
## Enunciado
Realizar el programa que sea capaz mediante una función mostrar si los siguientes años són bisiestos: ``[1600, 1900, 2000, 2016, 1987, 2100]``



### Pistas
1 Si el año es uniformemente divisible por 4, vaya al paso 2. De lo contrario, vaya al paso 5.
2 Si el año es uniformemente divisible por 100, vaya al paso 3. De lo contrario, vaya al paso 4.
3 Si el año es uniformemente divisible por 400, vaya al paso 4. De lo contrario, vaya al paso 5.
4 El año es un año bisiesto (tiene 366 días).
5 El año no es un año bisiesto (tiene 365 días).

La información se ha consultado de la web: [https://docs.microsoft.com/es-es/office/troubleshoot/excel/determine-a-leap-year](https://docs.microsoft.com/es-es/office/troubleshoot/excel/determine-a-leap-year)

### Test data
#### Input data
N.A

#### Output
El resultado es el siguiente:
```
True
False
True
True
False
False
```

### Solución
El contenido del código se encuentra en el fichero: **main.py**

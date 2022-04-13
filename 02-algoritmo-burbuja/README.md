# Algoritmo Burbuja
## Enunciado
Realizar el programa que sea capaz de:
1. Ordenar un vector de 15 posiciones según el algoritmo de la burbuja.
```
procedimineto DeLaBurbuja(a0,a1..an)
    para i <- 1 hasta n-1 hacer
        para j <- 0 hasta n-i-1 hacer
            si a(j) > a(j+1) entonces
                aux <- a(j)
                a(j) <- a(j+1)
                a(j+1) <- aux
            fin si
        fin para
    fin para
fin procedimineto
```
### Pistas
N.A.

### Test data
#### Input data
Se introduce el vector:`[32, 49, 37, 45, 59, 6, 41, 48, 65, 44, 12, 3, 74, 45, 83]`

#### Output
El resultado es el siguiente:
```
[3, 6, 12, 32, 37, 41, 44, 45, 45, 48, 49, 59, 65, 74, 83]
```

### Solución
El contenido del código se encuentra en el fichero: **main.py**

### Referencias
[Algoritmo de la burbuja](https://es.wikipedia.org/wiki/Ordenamiento_de_burbuja)
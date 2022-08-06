# Encriptar texto
## Enunciado
Realizar el programa que sea capaz mediante tres argumentos realizar:
1. El primer argumento tendra los posibles valores: sha1 y check
2. Si se informa sha1, el segundo argumento es el texto que va a devolver encriptado con SHA1.
3. Si se informa check, se tiene que informar dos argumentos:
   1. El primero es el texto sin encriptar
   2. El segundo es el texto encriptado 
   3. EL RESULTADO sera un mensaje de si coinciden o no los dos textos.


* Se utilizaran los módulos: sys(para los argumentos del script) y hashlib(para encriptar el texto).
* Se tiene que utilizar todo lo aprendido anteriormente.

### Pistas
* Para recuperar los argumentos es sys.argv es una lista
* Para poder encriptar se utilizara la función: `hashlib.sha1("texto a encriptar".encode()).hexdigest()`
* Controlar primero el numero de argumentos y despues los definidos en sys.argv[1]


### Test data
#### Input data
1. Se ejecuta el proceso: `main.py sha1 python-cuffy`
2. Se ejecuta el proceso: `main.py sha1 `
3. Se ejecuta el proceso: `main.py`
4. Se ejecuta el proceso: `main.py check python-cuffy 85d3383e3a2fb45eb7d0066a4879a9dad0`
5. Se ejecuta el proceso: `main.py check python-cuffy cc15110eb8a18b490e8b5a4a77093771d5ea30fe`

#### Output
1. El resultado es el siguiente: 
```
0d4e9039123e5d97af009e59345fb02a82d047fb
```
2. El resultado es el siguiente: *sin resultado*
3. El resultado es el siguiente: 
``` 
Primer argumento no valido, los posibles: ['sha1', 'check']
```
4. El resultado es el siguiente: `Los textos no coinciden.`
5. El resultado es el siguiente: `Los textos coinciden!`

### Solución
El contenido del código se encuentra en el fichero: **main.py**

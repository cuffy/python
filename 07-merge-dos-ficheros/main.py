from os import mkdir
from os.path import exists
import hashlib
import funciones
LINES = 10

"Si la carpeta no existe se crea"
if not exists("./data"):
    mkdir("./data")

funciones.create_files("data/file_a.txt", LINES)
funciones.create_files("data/file_b.txt", LINES)

funciones.merge_files("data/file_c.txt", "data/file_a.txt", "data/file_b.txt")

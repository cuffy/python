import hashlib

"Una forma de trabajar con los ficheros con abrir el fichero y cerrar una vez finalizado la operación"
def create_files(name_file, lines):
    f = open(name_file, "w")
    for i in range(lines):
        text = "printhelloworld.dev--" + str(i)
        f.write(hashlib.sha256(text.encode()).hexdigest() + "\n")
    f.close()


"Otra forma de trabajar con los ficheros y es con la sentencia de with"
def merge_files(name_file_c, name_file_a, name_file_b):
    content = ""
    for nf in [name_file_a, name_file_b]:
        with open(nf) as f:
            content += f.read()
    with open(name_file_c, "w") as f:
        f.write(content)
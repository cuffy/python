from password import Password

pswd = Password()

LENGTH = 8

print("Tu clave de digitos es:", pswd.generate(LENGTH, Password.DIGITS))
print("Tu clave de string es:", pswd.generate(LENGTH, Password.STRINGS))
print("Tu clave de numeros y string es:", pswd.generate(LENGTH, Password.ALPHABET))
print("Tu clave es:", pswd.generate(LENGTH, Password.ALL))
print()
print("Se ha generado un token:", pswd.generate_token())

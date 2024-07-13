"""
2) Crear un programa que solicite al usuario que ingrese una contraseña
mediante prompt.
Comprobar que la contraseña ingresada sea ‘utn750’. En caso de no
coincidir, volver a solicitarla hasta que coincidan.

"""
clave = input("login","ingrese la clave")
while clave != "utn750":
    clave = input("Error==>"," ingrese la clave nuevamente")
print("La clave es correcta",clave)
    
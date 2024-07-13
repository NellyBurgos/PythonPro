""""
3) Crear un programa que solicite al usuario que ingrese un número.
Se deberá validar que se encuentre entre 0 y 9 inclusive. En caso no
coincidir con el rango, volverlo a solicitar hasta que la condición se cumpla.

"""
numero=int(input("Ingrese un numero (entre 0 y 9): "))
while numero < 1 or numero > 9:
    print("Error no concide con el rango.Ingrese el numero nuevamente: ")
    numero=int(input("Ingrese un numero (entre 0 y 9): "))
print("El numero coincide con el rango:",numero)
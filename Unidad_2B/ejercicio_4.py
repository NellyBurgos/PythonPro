"""""
4) Crear un programa que solicite al usuario que ingrese una letra. Se deberá
validar que la letra sea ‘U’, ‘T’ o ‘N’ (en mayusculas).
En caso no coincidir con ninguna de las letras, volver a solicitarla hasta que
la condición se cumpla
"""
letra = "'U''T'o'N'"
letra=input("Ingrese la  letra : ")
while letra != 'U''T''N':
    print("Error==> la letra posibles son: 'U T N' ")
    letra=input("Ingrese la letra : ")
print("La letra ingresada es correcta 'U''T''N': ",letra)
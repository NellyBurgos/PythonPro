""""
5) Crear un programa que solicite 5 números mediante prompt. Calcular la
suma acumulada y el promedio de los números ingresados.

"""
suma_acumulada = 0
contador = 0
while contador < 5:
    numero =int(input("Ingrese un numero: "))
    suma_acumulada += numero
    contador += 1

promedio = suma_acumulada / 5
print("La suma acumulada es:",suma_acumulada)
print("El promedio es:",promedio)
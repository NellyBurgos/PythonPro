""""
Ahora el siguiente desafío consiste en hacer que el programa que tuvimos de prueba muestre
tanto el valor máximo ingresado como el minimo.
Ahora.. si lograste realizarlo utilizando el código de muestra hasta el momento, 
¿Qué sucede si ingresamos números consecutivos como 1,2,3,4?

"""
contador=0
min_numero = float('inf')   
max_numero = float('-inf')   

while contador < 4:
    num = int(input("ingrese un numero:"))

    if num < min_numero:
        min_numero = num
   
    if num > max_numero:
        max_numero = num
    contador+=1
print("Cantidad de numero ingresado: ",contador)
print("el valor minimo es: ", min_numero)
print("el valor maximo es: ", max_numero)

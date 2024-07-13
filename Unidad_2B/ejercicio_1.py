"""
1) Crear un programa que pueda sumar los números pares comprendidos
entre el 1 y el 10.

"""
suma = 0   
numero = 1 

while numero <= 10:       
    if numero % 2 == 0:   
        suma += numero    
    numero += 1        
print("La suma de los números pares entre 1 y 10 es: ", suma)

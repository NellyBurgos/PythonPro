"""
Escribe un programa que muestre por pantalla el resultado de la siguiente
operación (10+3) * (6+6), ¿qué sucede si realizas la misma operación pero sin
los paréntesis?

"""

resultado_con_parentesis = (10+3) * (6+6) #Si no se utilizan paréntesis, las operaciones se realizan
                                          #siguiendo la jerarquía de operadores, en este caso, 
                                          # #primero la multiplicación y luego la suma

print("EL resultado de la operacion es:",resultado_con_parentesis)
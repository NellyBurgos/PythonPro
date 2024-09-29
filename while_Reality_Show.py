
"""
De los 3 Jugadores de un Reality Show, se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibió en la etapa de votos
Informar:
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan mediante input()
"""

nombre = ""
edad = 0   
votos = 0   
nombre_max_votos = ""   
max_votos = float('-inf')
nombre_min_votos = ""  
min_votos = float('inf')
total_edades = 0  
total_votos = 0   
cantidad_candidatos = 3  

contador_candidatos = 0
while contador_candidatos < 3:
    nombre = input("Ingrese el nombre del candidato  : ")
    edad = int(input("Ingrese la edad del candidato (mayor 25): "))
    while edad < 25:
        print("Error ==> la edad debe ser mayor a 25 .Ingrese nuevamente la edad del candidato: ")
        edad = int(input("Ingrese la edad del candidato (mayor 25): "))
    votos = int(input("Ingrese la cantidad de votos (mayor o igual a cero): "))
    while votos < 0:
        print("Error ==> La cantidad de votos no puede ser menor a cero .Ingrese nuevamente la cantidad de votos: ")
        votos = int(input("Ingrese la cantidad de votos (mayor o igual a cero): "))
    if votos > max_votos:  
        max_votos = votos
        nombre_max_votos = nombre
    if votos < min_votos:  
        min_votos = votos
        nombre_min_votos = nombre
    total_edades += edad   
    total_votos += votos  
    contador_candidatos += 1 
promedio_edades = total_edades // 3  

print("a. El candidato con más votos es: ", nombre_max_votos, "con", max_votos, "votos") 
print("b. El candidato con menos votos es: ", nombre_min_votos, "con" , min_votos, "votos") 
print("c. El promedio de edades de los candidatos es: ", promedio_edades) 
print("d. El total de votos emitidos es: ", total_votos) 

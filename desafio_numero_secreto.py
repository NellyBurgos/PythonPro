"""""
Tu tarea es crear el código teniendo en cuenta los siguientes puntos:

pedirá al usuario que ingrese un número entero;utilizará un bucle while;
comprobará si el número ingresado por el usuario es el mismo que el número escogido por el mago. 
Si el número elegido por el usuario es diferente al número secreto del mago, el usuario debería ver el mensaje
"¡Ja, ja! ¡Estás atrapado en mi bucle!" y se le solicitará que ingrese un número nuevamente. 
Si el número ingresado por el usuario coincide con el número escogido por el mago, 
el número debe imprimirse en la pantalla, y el mago debe decir las siguientes palabras:
 "¡Bien hecho, Junior! Eres libre ahora."
"""
print(
"""
+================================+
| ¡Bienvenido a mi juego, Junior!|
| Introduce un número entero |
| y adivina qué número he |
| elegido para ti. |
|¿Cuál es el número secreto? |
+================================+
""")
secret_number = 777

while True:
    numero=int(input("Ingrese un numero: "))
    if numero != secret_number:
       print("¡Ja, ja! ¡Estás atrapado en mi bucle!. Intenta de nuevo")
    else:
       print("¡Bien hecho, Junior! Eres libre ahora. ")
       break
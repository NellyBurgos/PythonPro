import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random

'''
nombre:Nelly
apellido: Burgos
---
Ejercicio: for_09
---
Enunciado:
Al comenzar el juego generamos un número secreto del 1 al 100, se pedira al usuario el ingreso de un numero por prompt y si el número ingresado es el mismo que el número secreto se dará por terminado el juego con un mensaje similar a este: 

En esta oportunidad el juego evaluará tus aptitudes a partir de la cantidad de intentos, por lo cual se informará lo siguiente:
    1° intento: “Usted es un psíquico”.
	2° intento: “Excelente percepción”.
	3° intento: “Esto es suerte”.
	4° hasta 6° intento: “Excelente técnica”.
	7 intentos: “Perdiste, suerte para la próxima”.

de no ser igual se debe informar si 
“Falta…”  para llegar al número secreto  o si 
“Falta…”  del número secreto.

'''' ' 

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
         
         import random
         numero_secreto = random.randint(1, 100)
         
         intentos=0
         print("¡Bienvenido al juego de adivinanza de números!")
         
         while True:
             intentos += 1
             numero_ingresado= int(prompt("","Ingresa un número entre 1 y 100:"))
             while numero_ingresado < 1 or numero_ingresado > 100:
                print("El número debe estar entre 1 y 100. Intenta de nuevo.")
                numero_ingresado= int(prompt("","Ingresa un número entre 1 y 100:"))

             if numero_ingresado == numero_secreto:
                 if intentos == 1:
                     mensaje = "Usted es un psíquico"
                 elif intentos == 2:
                     mensaje = "Excelente percepción"
                 elif intentos == 3:
                     mensaje = "Esto es suerte"
                 elif intentos <= 6:
                     mensaje = "Excelente técnica"
                 else:
                     mensaje = "Perdiste, suerte para la próxima"
                     
                 print(f"¡Felicidades! Adivinaste el número secreto ({numero_secreto}) en {intentos} intentos. {mensaje}")
                 break
             
             elif numero_ingresado < numero_secreto:
                 print("Falta... para llegar al número secreto.")
             else:
                 print("Falta... del número secreto.")
             
             if intentos == 7:
                 print(f"Perdiste, suerte para la próxima. El número secreto era {numero_secreto}.")
                 break
         
                
            
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
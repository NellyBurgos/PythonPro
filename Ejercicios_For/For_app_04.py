import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Nelly
apellido:Burgos
---
Ejercicio: for_04
---
Enunciado:
Al presionar el botón 'Mostrar' pedir 10 valores por prompt o hasta que el usuario ingrese el valor 9 (se deberá utilizar 'BREAK').
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):


         for i in range(10):
           valor = int(prompt("","Ingrese un valor (9 para salir): "))
           if valor == 9:
             break
         print("Valores ingresados:", valor)
        


        


        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Nelly
apellido:Burgos
---
Ejercicio: listas_01
---
Enunciado:
Al presionar el botón  'Mostrar', se deberán mostrar los números 
almacenados en la lista_datos utilizando Dialog Alert para informar cada elemento.
(Utilizar 'for in range' y 'for in')
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

        self.lista_datos = [2,3,5,7,11,13]


    def btn_mostrar_on_click(self):
        lista_datos = [23, 56, 12, 78, 45]

        # Utilizando 'for in range'
        for i in range (len( lista_datos)):
            alert("Mostrar",lista_datos[i])
        
        # Utilizando 'for in'
        for dato in lista_datos:
            alert("Mostrar",dato)
        
                
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
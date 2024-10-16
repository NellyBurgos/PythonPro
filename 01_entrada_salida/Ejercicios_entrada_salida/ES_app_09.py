import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Nelly
apellido: Burgos
---
Ejercicio: entrada_salida_09
---
Enunciado:
Al presionar el botón 'Calcular', se deberá obtener el valor contenido en la caja de texto (txtSueldo), 
transformarlo a número y mostrar el importe de sueldo actualizado con el incremento del 15% utilizando el Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="sueldo")
        self.label1.grid(row=0, column=0, padx=20, pady=10)

        self.txt_sueldo = customtkinter.CTkEntry(master=self)
        self.txt_sueldo.grid(row=0, column=1)

        self.btn_mostrar = customtkinter.CTkButton( master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, padx=30, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        sueldo_texto = self.txt_sueldo.get()

        sueldo_numero =float(sueldo_texto)

        incremento = sueldo_numero  * 15 / 100
        total = sueldo_numero + incremento

        message =f"El sueldo  es:",format(total)
        alert("calcular",message=message)     

if __name__=="_main_":
     app = App()
     app.geometry("300x300")
     app.mainloop()






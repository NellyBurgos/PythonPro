import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Nelly
apellido: Burgos
---
Ejercicio: entrada_salida_10
---
Enunciado:
Al presionar el botón  'Calcular', se deberá obtener el valor contenido en la caja de texto (txt_importe), 
transformarlo a número y mostrar el importe actualizado con un descuento del 20% utilizando el Dialog Alert.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Importe")
        self.label1.grid(row=0, column=0, padx=20, pady=10)

        self.txt_importe = customtkinter.CTkEntry(master=self)
        self.txt_importe.grid(row=0, column=1)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, padx=30, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        valor_texto = self.txt_importe.get()
        valor_numero =float(valor_texto)
        descuento = valor_numero * 20 / 100
        total=  valor_numero - descuento

        message ="El precio con descuento es:",format(total)

        alert(title="calcular", message=message)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: while_09
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera 
hasta que presione el botón Cancelar (en el prompt). 
Luego determinar el máximo y el mínimo 
e informarlos en los cuadros de textos txt_maximo y txt_minimo respectivamente

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.txt_minimo = customtkinter.CTkEntry( master=self, placeholder_text="Mínimo")
        self.txt_minimo.grid(row=0, padx=20, pady=20)

        self.txt_maximo = customtkinter.CTkEntry(master=self, placeholder_text="Máximo")
        self.txt_maximo.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")

    def btn_comenzar_ingreso_on_click(self):
        minimo = self.txt_minimo.get()
        maximo = self.txt_maximo.get()

        minimo= float('inf')
        maximo= -float('inf')
        contador=0
        while True:
            entrada=(prompt("","Numero ['cancelar'para terminar]: "))
            if entrada=='cancelar':
               break
            numero = float(entrada) 
            contador+=numero
        
            if numero > maximo:
                maximo = numero
        
            if numero < minimo:
                minimo = numero
        
        alert("El numero maximo es:", message=maximo)
        alert("El numero minimo es:", message=minimo)



""""

        numeros = []
        numero = prompt("","Ingrese un número (o presione Enter para finalizar): ")
        while numero != "":
            numeros=float(numero)
            numero = prompt("","Ingrese otro número (o presione Enter para finalizar): ")
            if numeros:
               maximo = max(numeros)
               minimo = min(numeros)
    
            alert("Máximo:", message=maximo)
            alert("Mínimo:", message=minimo)
"""

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

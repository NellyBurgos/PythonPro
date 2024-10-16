import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Nelly 
apellido: Burgos
---
Ejercicio: for_08
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. Mostrar cada número primo entre 1 y el número ingresado,
e informar la cantidad de números primos encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        pass

    def es_primo(n):
        
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    numero = int(prompt("","Ingresa un número: "))
    primos = []

    for num in range(2, numero + 1):
        if es_primo(num):
            primos.append(num)
    
    print("Números primos entre 1 y {}: {}".format(numero, primos))
    
    print("Cantidad de números primos encontrados: {}".format(len(primos)))

        

        
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
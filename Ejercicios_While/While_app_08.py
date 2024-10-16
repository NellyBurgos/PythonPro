import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Nelly
apellido:Burgos
---
Ejercicio: while_08
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera, 
hasta que presione el botón Cancelar (en el prompt) o el usuario ingrese cero. 
Calcular la suma acumulada de los positivos y multiplicar los negativos. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_producto

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_producto = customtkinter.CTkEntry(master=self, placeholder_text="Producto")
        self.txt_producto.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        suma_acumulada = self.txt_suma_acumulada.get()
        producto_negativos = self.txt_producto.get()
        
        suma_acumulada = 0
        contador = 0
        producto_negativos = 1
        hay_negativos = False
        
        while True:
            entrada =prompt("","Introduce el número ( escribe 'cancelar' o cero para salir): ")
            if entrada == 'cancelar':
                break
            numero = float(entrada)  # Convierte la entrada a un número (int o float)
            suma_acumulada += numero
            contador += 1
            if numero < 0:
                producto_negativos *= numero
                hay_negativos = True
        if contador > 0:
            promedio= suma_acumulada / contador
            alert("Suma acumulada es:", message=suma_acumulada)
            alert("El promedio es:", message=promedio)
        else:
            alert("No se ingresaron números.")
        
        if hay_negativos:
            alert("El producto de los números negativos es:", message=producto_negativos)
        else:
            alert("No se ingresaron números negativos.")
        


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Nelly
apellido:Burgos
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
         sum_negativos = 0
         sum_positivos = 0
         cantidad_positivos = 0
         cantidad_negativos = 0
         cantidad_ceros = 0
         contador=0
         
         while True:
            entrada= prompt("","Ingresa el número ('cancelar' para salir): ")
            if entrada == 'cancelar':
              break
            numero = float(entrada)
            contador += numero
            if numero< 0:
              sum_negativos += numero
              cantidad_negativos += 1
            elif numero > 0:
              sum_positivos += numero
              cantidad_positivos += 1
            else:
              cantidad_ceros += 1
         diferencia = cantidad_positivos - cantidad_negativos 

         alert("A. Suma acumulada de los negativos:" ,message=sum_negativos)
         alert("B. Suma acumulada de los positivos:" ,message=sum_positivos)
         alert("C. Cantidad de números positivos ingresados:" ,message=cantidad_positivos)
         alert("D. Cantidad de números negativos ingresados:" ,message=cantidad_negativos)
         if cantidad_ceros:
            alert("E. La cantidad de numeros cero es:", message=cantidad_ceros)
         else:
            alert("E. No se ingresaron números cero:")
        
         alert("F. Diferencia entre la cantidad de números positivos ingresados y los negativos:" ,message=diferencia)

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

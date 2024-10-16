import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Nelly
apellido: Burgos
---
TP: IF_Iluminacion
---
Enunciado:
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        self.title("UTN")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        marca = self.combobox_marca.get()
        cantidad_texto = self.combobox_cantidad.get()
        cantidad_numero=int(cantidad_texto)
        
        descuento=0
        ahorro_ad=0
        
        if cantidad_numero >= 6:
            descuento = 0.50

        elif cantidad_texto == 5:
            if marca == "ArgentinaLuz":
                descuento = 0.40
            else:
                descuento = 0.30

        elif cantidad_numero== 4:
            if marca =="ArgentinaLuz" or marca == "FelipeLamparas":
                descuento = 0.25
            else:
                descuento = 0.20
        elif cantidad_numero== 3:
            if marca == "ArgentinaLuz":
                descuento = 0.15
            elif marca == "FelipeLamparas":
                descuento = 0.10
            else:
                descuento = 0.05


        sub_total= 800 * cantidad_numero
        ahorro= sub_total * descuento/100
        total_con_descuento= sub_total- ahorro
        
        if total_con_descuento > 4000:
            ahorro_ad= total_con_descuento * 5 / 100
        total_a_pagar= total_con_descuento-ahorro_ad

    
        mensaje ="La cantidad es: {1}\n La marca es: {0}\n El descuento es: {2}% \n Total (s/desc) es: {3} %\n El ahorro fue: {4} $\n Total: {5} $\n Ahorro adicional (5%) es: {6} $ \n\n TOTAL a pagar: {7} $".format(marca,cantidad_numero,descuento,sub_total,ahorro,total_con_descuento,ahorro_ad,total_a_pagar)
        alert(title="TEST",message=mensaje)
    

        

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
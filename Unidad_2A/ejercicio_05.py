""""
5) Crear un programa que al ingresar un número puede calcular si es mayor,
niño/a(menor de 10) o pre-adolescente (edad entre 10 y 13 años)
adolescente (edad entre 13 y 17 años) de edad.

"""
edad=int(input("Ingrese la edad: "))
if edad <10:
    print("Niño/a menor de 10 años")
elif edad >=10 and edad <= 13:
    print(" Es pre-adolecente tenes entre 10 y 13 años")
elif edad >=13 and edad <=17:
    print("Es  adolecente tenes 13 y 17 años" )
elif edad >=18:
    print("Es mayor de edad")
else:
    print("Es menor de edad ")
     
        
        

""""
Para el departamento de facturación:
A. Ingresar tres precios de productos y mostrar la suma de los mismos.
B. Ingresar tres precios de productos y mostrar el promedio de los mismos.
C. ingresar tres precios de productos sumarlos y mostrar el precio final (más IVA 21%).

"""
producto1 = float(input("Ingrese el precio del producto 1:"))
producto2 = float(input("Ingrese el precio del producto 2:"))
producto3 = float(input("Ingrese el precio del producto 3:"))

print("La suma de los tres precio es: ",producto1 + producto2 + producto3,"$")
print("El promedio de los tres precio es: ",(producto1 + producto2 + producto3) // 3 ,"$")
print("El final con IVA es: ",(producto1 + producto2 + producto3) * 1.21, "$")


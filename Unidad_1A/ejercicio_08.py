""""
Cree un programa que permite ingresar el nombre de un producto, el
precio y que calcule el IVA.

"""
iva_porcentaje = 0.21

nombre_producto = input("Ingrese el nombre del producto:")
precio_producto = float(input("Ingrese el precio:"))

iva = precio_producto * iva_porcentaje
precio_total = precio_producto + iva

print("El nombre del producto:",nombre_producto )
print(" tiene un precio de:",precio_producto)
print("El iva aplicado es:",iva)
print("El precio total con IVA incluido es de:",precio_total)

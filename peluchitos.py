peluches=["roshi","conejito","aguacatico"]
opcion=0

print("Pelucheria PELUCHITOS")
print(".....................")
print("1. Agregar Producto a la bodega")
print("2. Ver productos en bodega")
print("3. Obtener del inventario")
print("4. Ver productos mas vendidos")
print("5. SALIR")

while(opcion!=5):
    opcion=opcion+1
    opcion=int(input("digita un numero: "))
    if opcion==1:
        nombre=input("Digita el nombre del producto: ")
        #Agregando datos a una lista.
        peluches.append(nombre)
        print("Peluche agregado con exito")
    elif opcion==2:
        print(peluches)
    elif opcion==3:
        print("Usted esta en la opción 3")
    elif opcion==4:
        print("Usted esta en la opción 4")
    elif opcion==5:
        print("Chao")
    else:
        print("Valor no valido")
print("sali del siclo")

    

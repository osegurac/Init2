Opcion = int(input("Que desea hacer? \n 1-Agregar \n 2-Salir \n"))
Lista = []
while True:
    if Opcion == 1:
        Producto = input("Producto ")
        Precio = int(input("Precio "))
        Lista.append(Producto)
        Lista.append(Precio)
        break
    elif Opcion == 2:
        break
print(Lista)
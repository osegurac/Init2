Opcion = int(input("Que desea hacer? \n 1-Agregar \n 2-Salir \n"))
Lista = []
while True:
    if Opcion == 1:
        Nombre = input("Nombre ")
        Nombre2 = input("Nombre 2 ")
        Nombre3 = input("Nombre 3 ")
        Nombre4 = input("Nombre 4 ")
        Nombre5 = input("Nombre 5 ")
        Nombre6 = input("Nombre 6 ")
        Lista.append(Nombre)
        Lista.append(Nombre2)
        Lista.append(Nombre3)
        Lista.append(Nombre4) 
        Lista.append(Nombre5)
        Lista.append(Nombre6)
        break
    elif Opcion == 2:
        break
print(Lista)
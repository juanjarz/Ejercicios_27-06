lista = []
while True:
    decision = input("Ingrese 'Si', si desea agregar un usuario o escriba cualquier otra palabra para salir: ")
    if decision in ("Si", "sI", "SI", "si"):
        nombre = (input('Ingrese el nombre para la lista: ')).lower()
        lista.append(nombre)
    else:
        break
nom = (input('Ingresa el nombre a buscar en la lista: ')).lower()
if nom in lista:
    print('El nombre se encuentra en la lista')
else:
    print('El nombre no se encuentra en la lista')
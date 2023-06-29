lista = []
while True:
    decision = input("Ingrese 'Si', si desea agregar un usuario o escriba cualquier otra palabra para salir: ")
    if decision in ("Si", "sI", "SI", "si"):
        nombre = input('Ingrese el nombre deseado: ')
        lista.append(nombre)
    else:
        break
if lista:
    print(f'La lista es: {lista}')
    print(f'La tupla es: {tuple(lista)}')
    print(f'El set es: {set(lista)}')
else:
    print('No hay elementos en la lista')


nom = (input('Ingresa el nombre repetido:')).lower()
lista = []
conteo = 0
while True:
    decision = input("Ingrese 'Si', si desea agregar un usuario o escriba cualquier otra palabra para salir: ")
    if decision in ("Si", "sI", "SI", "si"):
        nombre = (input('Ingrese el nombre para la lista: ')).lower()
        lista.append(nombre)
        if nombre == nom:
            conteo += 1
    else:
        break
print(f'El numero de veces que se repite el nombre es: {conteo}')
num_min = int(input('Ingrese el numero minimo: '))
num_max = int(input('Ingrese el numero maximo: '))
if num_min >= num_max:
    print('El rango no es el correcto')
else:
    for num in range(num_min, num_max +1):
        if num % 3 ==0:
            print(num)
num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))
num3 = int(input('Ingrese el tercer numero: '))

if num1 == num2 == num3:
    print(f'El resultado es: {(num1+num2+num3)*3}')
else:
    print(f'El resultado es: {num1+num2+num3}')
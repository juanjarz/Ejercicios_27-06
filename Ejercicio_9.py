texto = input('Ingrese el texto a analizar: ')
cont_num = False

for caracter in texto:
    if caracter.isdigit():
        cont_num = True
        break

if cont_num:
    print("El texto contiene números.")
else:
    print("El texto no contiene números.")
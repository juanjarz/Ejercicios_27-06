segundos = float(input('Ingrese la cantidad de segundos que desea convertir: '))
horas = float(segundos//3600)
minutos = float(segundos%3600)//60
segundos_restantes = (segundos % 3600) % 60


print(f'''Los segundos dados equivale a {horas} horas,{minutos} minutos y {segundos_restantes} segundos''')
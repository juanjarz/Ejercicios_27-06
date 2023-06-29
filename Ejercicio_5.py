while True:
    letra = (input("Ingrese la letra a analizar: ")).lower()
    if letra in ("a", "e", "i", "o","u"):
        print('La letra es vocal')
        break
    else:
        print('La letra no es vocal')
        break
        
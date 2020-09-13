valores = []
while True:
    numero = int(input("numero: "))
    if numero != -1:
        valores.append(numero)
    else:
        print(valores)
        break
print (*valores, sep=(";"))
valores.reverse()
print(*valores, sep=("#"))
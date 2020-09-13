valores = []
# Capturando os valores/itens da lista.
while True:
    numero = float(input("numero: "))
    if numero != -1:
        valores.append(numero)
    else:
        print(valores)
        break
# Mudando o separador da lista de "," para ";".
print (*valores, sep=(";"))
# Revertendo a ordem da lista e mudando o separador da mesma de "," para "#".
valores.reverse()
print(*valores, sep=("#"))
#Somando os itens ou valores da lista.
soma = sum(valores)
print(soma)
#Calculando média dos valores
media = soma/ len(valores)
print(media)
maior = []
for valor in valores:
    if valor > media:
        maior.append(valor)
print(maior)
print("O progama foi finalizado com sucesso")
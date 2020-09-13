#Capturando valores da lista e fazendo uma copia da mesma.
numeros = []
for voltar in range(10):
    valor = int(input("numero "))
    numeros.append(valor)
print(numeros)
copia_lista = numeros [:]
print(copia_lista)
maior50 = []
for unidade in copia_lista:
    if unidade > 50:
        maior50.append(unidade)
print(maior50)
if len(maior50) == 0:
    print("Alista não apresenta elementos maiores que o número 50.")
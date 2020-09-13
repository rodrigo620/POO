#Capturando valores da lista e fazendo uma copia da mesma.
numeros = []
for voltar in range(10):
    valor = int(input("numero "))
    numeros.append(valor)
copia_lista = numeros [:]
# A) Exibindo os indices do numeros maiores que 50.
maior50 = []
for a in copia_lista:
    if a > 50:
        maior50.append(a)
        pass
if len(maior50) != 0:
        print(maior50)
        pass
if len(maior50) == 0:
    print("Alista não apresenta elementos maiores que o número 50.")
    pass
# B) Removendo elementos entre 10 e 20.
intervalo = []  
remoção = copia_lista [:]
for b in remoção:
   if b > 10 and b < 20:
        intervalo.append(b)
        remoção.remove(b)
        pass
if len(intervalo) == 0:
        print("A lista não apresenta elementos no intervalo entre 10 e 20.")
        pass
print(remoção)
# C) Informando quantas vezes um numero aparece na lista.
repetição = 0
lista = set(copia_lista)
for c in lista:
        repetição = copia_lista.count(c)
        print("O número %s aparece %s vez(es)." %(c,repetição))
        pass
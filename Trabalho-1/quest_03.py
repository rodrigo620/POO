#Recebendo a temperatura média mensal.
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
temperatura_meses = []
for mes in range(len(meses)):
    temperatura = int(input("Informe a temperatura média em %s: " %meses[mes]))
    temperatura_meses.append(temperatura)
    pass
# Calculando a temperatura média anual.
temperatura_media = (sum(temperatura_meses))/ (len(temperatura_meses))
print("Média anual = %sº C" %temperatura_media)
#Exibindo meses em que a temperatura foram acima da média anual.
sequencia = 0
for voltas in range(len(meses)):
    if temperatura_meses[voltas] > temperatura_media:
        sequencia = sequencia + 1
        print("%s° Mês = %s (%sº C)" %(sequencia, meses[voltas], temperatura_meses[voltas]))
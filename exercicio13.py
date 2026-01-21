#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
temperaturas = []
meses = {
    1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
    5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
    9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
}
for i in range(12):
    temperatura = float(input("Digite a temperatura média do mês {}: ".format(meses[i+1])))
    temperaturas.append(temperatura)
media_anual = sum(temperaturas) / len(temperaturas)
print("\nTemperaturas acima da média anual:")
for i in range(12):
    if temperaturas[i] > media_anual:
        print("{} - {}: {:.2f}°C".format(i+1, meses[i+1], temperaturas[i]))
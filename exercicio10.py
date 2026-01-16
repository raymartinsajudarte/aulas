#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados
# 11% para o Imposto de Renda
# 8% para o INSS e 5% para o sindicato
# faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$

valorHora = float(input("Digite o seu salário recebido por horas trabalhadas: "))
horasTrabalhadas = float(input("Digite a quantidade de horas trabalhadas este mês: "))
valorTotal = valorHora * horasTrabalhadas
impostoderenda = valorTotal*0.11
inss = valorTotal*0.08
sindicato = valorTotal*0.05
salarioLiquido = valorTotal - impostoderenda - inss - sindicato
print("O valor total do seu salário bruto recebido este mês é de: ", valorTotal)
print("Imposto de Renda: ", impostoderenda)
print("INSS: ", inss)
print("Sindicato: ", sindicato)
print("salario liquido: ", salarioLiquido) 
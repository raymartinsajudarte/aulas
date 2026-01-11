#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
valorHora = float(input("Digite o seu salário recebido por horas trabalhadas: "))
horasTrabalhadas = float(input("Digite a quantidade de horas trabalhadas este mês: "))
valorTotal = valorHora * horasTrabalhadas
print("O valor total do seu salário recebido este mês é de: ", valorTotal)
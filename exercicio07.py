#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
farenheit = float(input("Digite a temperatura em farenheit que você deseja converter em Celsius: "))
celsius = 5 * (farenheit - 32) / 9
print("A temperatura convertida de Farenheit para Celsius é: ", celsius)
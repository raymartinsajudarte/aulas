#Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
idades = []
alturas = []
print("Digite as idades e alturas dos 30 alunos")
for i in range(30):
    idade = int(input("Digite a idade do aluno {}: ".format(i+1)))
    altura = float(input("Digite a altura do aluno {} (em metros): ".format(i+1)))
    idades.append(idade)
    alturas.append(altura)
media_altura = sum(alturas) / len(alturas)
contador = 0
for i in range(30):
    if idades[i] > 13 and alturas[i] < media_altura:
        contador += 1
print("\nNúmero de alunos com mais de 13 anos e altura inferior à média de altura dos alunos:", contador)


#utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?"
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
respostas = []
print("Responda 's' para sim ou 'n' para não para as seguintes perguntas:")
perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]
for pergunta in perguntas:
    resposta = input(pergunta + " ").lower()
    while resposta not in ['s', 'n']:
        print("Responda apenas 'sim' ou 'não'.")
        resposta = input(pergunta + " ").lower()
    respostas.append(resposta)
num_sim = respostas.count('s')
if num_sim == 2:
    print("\nClassificação: Suspeita")
elif 3 <= num_sim <= 4:
    print("\nClassificação: Cúmplice")
elif num_sim == 5:
    print("\nClassificação: Assassino, prenda-o imediatamente! >:(")
else:
    print("\nClassificação: Inocente")
while True:
    nome = input("Digite seu nome (maior que 3 caracteres): ")
    if len(nome) > 3:
        break
    else:
        print("Erro: O nome deve ter mais de 3 caracteres. Por favor, tente novamente.")

while True:
    try:
        idade = int(input("Digite sua idade (entre 0 e 150): "))
        if 0 <= idade <= 150:
            break
        else:
            print("Erro: A idade deve estar entre 0 e 150. Por favor, tente novamente.")
    except ValueError:
        print("Erro: Por favor, digite um número inteiro para a idade.")

while True:
    try:
        salario = float(input("Digite seu salário (maior que zero): "))
        if salario > 0:
            break
        else:
            print("Erro: O salário deve ser maior que zero. Por favor, tente novamente.")
    except ValueError:
        print("Erro: Por favor, digite um valor numérico para o salário.")

while True:
    sexo = input("Digite seu sexo ('f' ou 'm'): ").lower()
    if sexo == 'f' or sexo == 'm':
        break
    else:
        print("Erro: O sexo deve ser 'f' ou 'm'. Por favor, tente novamente.")

while True:
    estado_civil = input("Digite seu estado civil ('s', 'c', 'v' ou 'd'): ").lower()
    if estado_civil in ['s', 'c', 'v', 'd']:
        break
    else:
        print("Erro: Estado civil inválido. Por favor, digite 's', 'c', 'v' ou 'd'.")

print("Informações validadas com sucesso!")

while True:
    n= input("Digite seu nome de usuário: ")
    s= input("Digite sua senha: ")

    if s!= n:
        print("Senha cadastrada com sucesso!")
        break
    else:
        print("Erro: A senha não pode ser igual ao nome de usuário. Por favor, tente novamente.")

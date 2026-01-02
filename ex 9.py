while True:
    n=float(input("Digite uma nota entre zero e dez: "))

    if 0<=n<=10:
        print("Valor válido!")
        break
    else:
        print("Valor inválido! Por favor, digite uma nota entre zero e dez.")

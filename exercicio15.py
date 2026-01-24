horaDia = int(input("Digite a hora do dia (0-23): "))
if horaDia >= 0 and horaDia <= 11:
    print("Bom dia!")
elif horaDia >= 12 and horaDia <= 17:
    print("Boa tarde!")
elif horaDia >= 18 and horaDia <= 23:
    print("Boa noite!")
else:
    print("Hora inválida. Por favor, insira um valor entre 0 e 23.")
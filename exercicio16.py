final_placa = int(input("Digite o último dígito da placa do veículo: "))
dia_semana = input("Digite o dia da semana (segunda, terca, quarta, quinta ou sexta): ")
if dia_semana == "segunda" and (final_placa == 1 or final_placa == 2):
    print("O veículo não pode circular hoje.")
elif dia_semana == "terca" and (final_placa == 3 or final_placa == 4):
    print("O veículo não pode circular hoje.")
elif dia_semana == "quarta" and (final_placa == 5 or final_placa == 6):
    print("O veículo não pode circular hoje.")
elif dia_semana == "quinta" and (final_placa == 7 or final_placa == 8):
    print("O veículo não pode circular hoje.")
elif dia_semana == "sexta" and (final_placa == 9 or final_placa == 0):
    print("O veículo não pode circular hoje.")
else:
    print("O veículo pode circular normalmente hoje.")
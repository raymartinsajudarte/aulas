#Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
vetor1 = []
vetor2 = []
vetor3 = []
print("Digite os elementos do primeiro vetor")
for i in range(10):
    elemento = int(input("Digite o {}º elemento: ".format(i+1)))
    vetor1.append(elemento)
print("\nDigite os elementos do segundo vetor")
for i in range(10):
    elemento = int(input("Digite o {}º elemento: ".format(i+1)))
    vetor2.append(elemento)
print("\nDigite os elementos do terceiro vetor")
for i in range(10):
    elemento = int(input("Digite o {}º elemento: ".format(i+1)))
    vetor3.append(elemento)
vetor_resultante = []
for i in range(10):
    vetor_resultante.append(vetor1[i])
    vetor_resultante.append(vetor2[i])
    vetor_resultante.append(vetor3[i])
print("\nVetor resultante intercalado:")
print(vetor_resultante)
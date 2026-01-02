s=0
q=0

while True:
    n=float(input("Digite um número (0 para sair): "))
    if n==0:
     break
    s+=n
    q+= 1
if q== 0:
    print("Nenhum número foi digitado.")
else:
    m= s/q
    print(f"Soma total dos números: {s}")
    print(f"Média dos números digitados: {m}")
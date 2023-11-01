n1 = float(input("nota 1: "))
n2 = float(input("nota 2: "))
n3 = float(input("nota 3: "))

media = (n1 + n2 + n3)/3

if media >= 6:
    print(f"Aprovado com média {media:.1f}")
else:
    print(f"Reprovado com média {media:.1f}")
print("Obrigado por utilizar nosso programa!")


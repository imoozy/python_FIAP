nota1 = float(input("Digite uma nota: "))
if nota1 >= 0 and nota1 <= 10:
    nota2 = float(input("Digite uma nota: "))
    if nota2 >= 0 and nota2 <= 10:
        media = (nota1 + nota2) / 2
        print(f"média = {media:.1f}")
        if media >= 6: 
            print("Aprovado")
        else:
            print("Reprovado")
    else:
        print("A segunda nota é invalida")
else:
    print("A primeira nota é invalida")
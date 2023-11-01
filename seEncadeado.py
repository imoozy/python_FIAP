print("1 - positivo, negativo ou nulo")
print("2 - Calcular desconto")
print("3 - maior entre 2 números")
print("0 - Sair")

opcao = int(input("Digite uma opção: "))

if opcao == 1:

    num = int(input("Digite um numero: "))
    if num > 0:
        print("Positivo")
    elif num < 0:
        print("Negativo")
    else:
        print("Nulo")

elif opcao == 2:
   compra = float(input("Digite o valora da compra: R$"))
   if compra > 300:
        compra_desconto = compra * 0.9
   else:
       compra_desconto = compra * 0.95
   print(f"Valor da compra.....: R$ {compra:.2f}\nValor atualizado.....: R$ {compra_desconto:.2f}")

elif opcao == 3:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    if num1 > num2:
        print(num1)
    else:
        print(num2)

elif opcao == 0:
    print("Obrigado por utilizar o nosso programa")
else: 
    print("Opção inválida")
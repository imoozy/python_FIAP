# n1 = int(input("Digite o primeiro número: ")) 
# n2 = int(input("Digite o segundo número: "))
# n3 = int(input("Digite o terceiro número: "))

# if n1 > n2 and n1 > n3:
#     print(n1)
# elif n2 > n1 and n2 > n3:
#     print(n2)
# else:
#     print(n3)

# print("O maior número é: ")





n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

maior = n1;
if n2 > maior:
    maior = n2

if n3 > maior:
    maior = n3

print(maior)


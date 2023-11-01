# ler um numero dado pelo usuário
num = int(input("Digite um numero: "))
mult = int(input("Digite um mult: "))
# calcular o proximo multiplo de 5
prox_mult = num // mult * mult + mult
# exibir o proximo multiplo de 5
print(prox_mult)
#saída de dados: interação do sistema com o usuário: PRINT
# Entrada de dados: interação do usuário com o sistema: Input


#usuario digita o valor
valor = int(input("Digite um valor:")) #input sempre lê dado string (texto)
resposta = valor + valor
print("Dobro = ", resposta)


# Usuario digita o valor
valor = input("digite um valor:")
# mostra o valor e o tipo
print(valor, type(valor))
# converte para inteiro
valor = int(valor)
# efetua o calculo do dobro
resposta = valor + valor
# mostra o valor e o tipo
print(valor, type(valor))
# mostra a respota
print("Resultado:", resposta)
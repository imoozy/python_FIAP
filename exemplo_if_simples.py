rm = str(input("Por favor, digite seu RM: "))
idade = int(input("Por favor, digite sua idade: "))

if idade >= 18:
    print(f"Sua participação foi autorizadam aluno de RM:", (rm))
    print(f"Mais intruções serão enviadas ao seu e-mail cadastrado na FIAP!")

else:
    print(f"Você não atingiu a maioridade para participar desta competição")
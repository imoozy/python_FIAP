# Digitar a quantia
# calcular a quantidade de cedulas de 100/ 50/ 20/ 10
# atualiza a quantia


quantia=int(input("Digite a quantia: R$ "))
ced100 = quantia // 100 #divide inteiro por 100

quantia = quantia % 100 #com o modulo é atualizado a quantia
ced50 = quantia // 50

quantia = quantia % 50
ced20 = quantia // 20

quantia = quantia % 20
ced10 = quantia // 10

print(f"R$ 100.00..... = {ced100}\n"
      f"R$ 50.00..... = {ced50}\n"
      f"R$ 20.00..... = {ced20}\n"
      f"R$ 10.00..... = {ced10}")


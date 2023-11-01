valor1 = int(8475.56)
valor2 = int(45.1)
valor3 = int(34955.95847)


# \n faz com que o conteúdo mude de linha dentro do mesmo print
print("Valor 1 =",valor1,"\nValor2 =" ,valor2,"\nValor3 =" ,valor3)

#format()
print("Valor 1 = {v1:10.2f} \nValor2 = {v2:10.2f} \nValor3 = {v3:10.2f} ".format(v1 = valor1, v2 = valor2, v3 = valor3))
#:.2f está padronizando com que todos os valores tenham no máximo duas casas decimais depois da virgula, e o 10 está para alinhar a direita da pagina por empurrar 10 caracteres 

print("Valor 1 = {v1:010.2f} \nValor2 = {v2:010.2f} \nValor3 = {v3:010.2f}".format(v1=valor1, v2=valor2, v3=valor3))

#printf
print(f"Valor1 = {valor1:10.1f} \nValor2 = {valor2:10.1f} \nValor3 = {valor3:10.1f} ")
#Com :.1f após a variável ocorre o mesmo efeito do format

#printf int
print(f"Valor1 = {valor1:5d} \nValor2 = {valor2:5d} \nValor3 = {valor3:5d} ")
#Com :5d após a variável faz com que tenha 5 casas, no caso 5bits

#printf porcentagem
print(f"Valor1 = %d\nValor2 = %d\nValor3 = %d" % (valor1,valor2,valor3))
#porcento é formatação de caracter %F = real %o = octal %d = inteiro e por ai vai



compra = float(input("Valor da compra: "))

if compra >= 300:

    totalDesc = compra * 0.1
    compra = compra * 0.9

    
    print(f"Total do desconto foi de {totalDesc}")

print(f"O valor da compra foi de {compra:.2f}")


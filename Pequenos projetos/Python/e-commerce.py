valor = 0

while True:
    print("Loja do zé pequeno")
    print("-------------------------------------")
    print("(1) Sabonete - R$ 2.00")
    print("(2) Shampoo - R$ 10.00")
    print("(3) Limpol - R$ 3.50")
    print("(4) Oleo - R$ 7.00")
    print("(5) Pão - R$ 6.30")
    print("-------------------------------------")

    print("Qual dos produtos você vai querer?")
    x = int(input())

    if x == 1:
        x = 2.00
    elif x == 2:
        x = 10.00
    elif x == 3:
        x = 3.50
    elif x == 4:
        x = 7.00
    elif x == 5:
        x = 6.30
    else: 
        print("Produto inválido")
        continue

    print(f"Você escolheu o produto por R${x}")
    valor += x  

    print(f"Seu valor atual é R${valor:.2f}" + (" - você paga frete grátis" if valor > 200 else " - com frete"))
    
    z = int(input("(1) pix - 10% de desconto, (2) boleto - 5% de desconto, (3) cartão: 3x sem juros, (4) parcelamento 3x com juros de 2,5% ao mes\n"))
    
    if z == 1:
        z = (valor * 10) / 100
        print("você tem " + str(z) + (" de desconto no PIX"))
    elif z == 2:
        z = (valor * 5) / 100
        print("você tem " + str(z) + (" de desconto no BOLETO"))
    elif z == 3:
        z = valor / 3
        print("você tem " + str(z) + (" em 3 vezes sem entradas e sem juros"))
    elif z == 4:
        j = valor * 0.025 * 3
        j = valor - j
        print("o valor da compra com juros é " + str(j))

    print("Você quer continuar a compra? ")
    print("S/N")
    y = input()

    if y.lower() == "n":
        break

print(f"Obrigado por comprar na loja do zé pequeno! O valor da sua compra foi de R${valor:.2f}")

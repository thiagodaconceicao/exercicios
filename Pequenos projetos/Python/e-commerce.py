valor = 0 # valor total da compra
quantidade = {} # A Quantidade a ser comprada

while True:
    print("Loja do Zé Pequeno")
    print("-------------------------------------")
    print("(1) Sabonete - R$ 2.00")
    print("(2) Shampoo - R$ 10.00")
    print("(3) Limpol - R$ 3.50")
    print("(4) Óleo - R$ 7.00")
    print("(5) Pão - R$ 6.30")
    print("-------------------------------------")

    print("Qual produto você deseja?")
    x = int(input())
    
    # valores de cada compra
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

    print("Quantidade desejada:")
    q = int(input())
    quantidade[x] = quantidade.get(x, 0) + q  #Atualiza a quantidade dos produtos na variavel "Quantidade"

    print("Deseja continuar comprando? (S/N)")
    y = input()

    if y.lower() == "n":
        break

for produto, qtd in quantidade.items():
    valor_produto = produto * qtd
    valor += valor_produto

    print(f"Produto: R${produto:.2f} x {qtd} = R${valor_produto:.2f}")

print(f"O valor total da sua compra é R${valor:.2f}")

print("Escolha a forma de pagamento:")
print("(1) PIX - 10% de desconto")
print("(2) Boleto - 5% de desconto")
print("(3) Cartão - 3x sem juros")
print("(4) Parcelamento - 12x com juros de 2,5% ao mês")

z = int(input())

if z == 1:
    desconto = (valor * 10) / 100
    valor -= desconto
    print(f"Você tem R${desconto:.2f} de desconto no PIX")
elif z == 2:
    desconto = (valor * 5) / 100
    valor -= desconto
    print(f"Você tem R${desconto:.2f} de desconto no BOLETO")
elif z == 3:
    parcelas = 3
    valor_parcela = valor / parcelas
    print(f"Você pode pagar em {parcelas} vezes sem entrada e sem juros de R${valor_parcela:.2f} cada")
elif z == 4:
    juros = valor * 0.025 * 12
    valor += juros
    print(f"O valor da compra com juros é R${valor:.2f}")

print("Obrigado por comprar na Loja do Zé Pequeno!")

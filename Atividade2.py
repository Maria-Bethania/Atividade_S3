# Desconto na Farmácia
produto1 = input("Digite o código, com 04 dígitos, do primeiro produto: ")
produto2 = input("Digite o código, com 04 dígitos, do segundo produto: ")
cod_0054 = float(input("Qual o valor do produto, em R$? "))
cod_n_0054 = float(input("Qual o valor do produto, em R$? "))

valor_total = cod_0054 + cod_n_0054

if produto1 == produto2:
    valor_total = valor_total - 5
    print(f"Seu desconto é de R$5,00 e o valor total de suas compras é de R$ {valor_total} reais.")
elif (produto1 != produto2) and (produto1  == "0054" or produto2 == "0054"):
    valor_total = valor_total - (valor_total * (50/100))
    print(f"Seu desconto é de 50% e o valor total de suas compras é de R$ {valor_total} reais.")
else:
    print(f"Infelizmente, não haverá descontos nessa compra! O valor total é de R${valor_total} reais.")




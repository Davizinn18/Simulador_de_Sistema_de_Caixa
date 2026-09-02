nome_cliente = str(input("Olá, seja bem vindo. Qual é seu nome? "))
total_compra = float(input("Qual foi o valor total da sua compra? "))
forma_pagamento = int(input("Qual a forma de pagamento?\n [1] Pix\n [2] Cartão\n Digite aqui:"))

if forma_pagamento == 1:
    pix = forma_pagamento
elif forma_pagamento == 2:
    cartao = forma_pagamento

if forma_pagamento == 1:
    desconto = total_compra * 0.10
elif forma_pagamento == 2 and total_compra >= 200:
    desconto = total_compra * 0.05
else:
    desconto = 0

total_pagar = total_compra - desconto

print("------------- Recibo -------------")
print(f" Cliente: {nome_cliente}\n Valor total da compra: {total_compra}")
print(f" desconto {desconto}\n Total a pagar: {total_pagar}")
print("----------------------------------") 
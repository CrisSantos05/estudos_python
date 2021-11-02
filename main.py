# Analise de vendas de loja
# se o valor da venda for maior que 5 mil o sistema dará 10% de desconto

valor_product = 500
valor_unitario = 10
soma_total = valor_product * valor_unitario
#print(soma_total == 5000)

if soma_total >= 5000:
    print('O valor de desconto é:', soma_total*10/100)
    total = soma_total - soma_total*10/100
    print('Valor a ser pago:', total)
else:
    print('Valor abaixo da faixa para desconto', soma_total)


# Controle de vendas com inputs e dados
nome_produto1 = input('Nome do Produto 1: ')
valor_produto1 = float(input("Insira o valor do produto: "))

print('__________________________________________________________________________________________')

nome_produto2 = input('Nome do Produto 2: ')
valor_produto2 = float(input("Insira o valor do produto: "))

print('__________________________________________________________________________________________')

nome_produto3 = input('Nome do Produto 3: ')
valor_produto3 = float(input("Insira o valor do produto: "))

print('__________________________________________________________________________________________')

total = valor_produto1 + valor_produto2 + valor_produto3

print('Total a pagar: ', total)

print('__________________________________________________________________________________________')

if total > 10:
    print('Valor total', total)
    desc = total*5/100
    tc = total - desc
    print('total de desconto: ', desc)
    print('total a pagar: ', tc)
else:
    print(total, 'Sem desconto')


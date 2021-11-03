import random

Pos = 'sim'

#Programa que faz loop de cadastro enquanto a pergunta de continuação for sim!


while Pos != 'não':

    print('Número de cadastro gerado: ',random.randrange(1,101))
    nome = input('Seu nome aqui: ')
    idade = int(input('Sua idade aqui: '))
    peso = float(input('Seu peso aqui: '))
    cont = input('Quer continuar ?: ')
    Pos = cont
    print('____________________________________________________________________________________________')

print('Cadastro Encerrado')


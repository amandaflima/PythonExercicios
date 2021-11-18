'''Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o
 programa vai informar quantas cédulas de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''
print('-' * 30)
print('{:^30}'.format('BANCO CEV'))
valor = int(input('Qual o valor a ser sacado? R$'))
total = valor
ced = 50
cont= 0
while True:
    if total >= ced:
        total -= ced
        cont +=1
    else:
        print(f'o total de {cont} cedulas de R${ced}')
        if ced == 50: #se ja acabou as possibilidades de ser 50, vai pras de 20 e assim por diante
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        cont = 0 #zerar o valor da quantidade de cada celula
        if total == 0:
            break
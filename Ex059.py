'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
op = 0
maior = 0
while op != 5:
    op = int(input('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    Qual operação voce deseja realizar? '''))
    if op == 1:
        print('A soma entre eles é {}'.format(n1+n2))
    elif op == 2:
        print('A multiplicação entre eles é {}'.format(n1*n2))
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior é {}'.format(maior))
    elif op == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
    else:
        print('Opção invalida! Tente Novamente')



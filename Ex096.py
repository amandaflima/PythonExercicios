#Faça um programa que tenha uma função chamada área(), que
# receba as dimensões de um terreno retangular (largura e comprimento)
# e mostre a área do terreno

def area(l, c):
    a = l * c
    print(f'A area é: {a}')


l = float(input('LARGURA DO TERRENO: '))
c = float(input('COMPRIMENTO DO TERRENO: '))
area(l, c)

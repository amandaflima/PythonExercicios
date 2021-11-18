# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
a1 = int(input('Qual o primeiro termo da PA? '))
r = int(input('Qual a razão da PA? '))
termo = a1
cont = 1
while cont<=10:
    print('{} '.format(termo), end='')
    termo += r
    cont += 1


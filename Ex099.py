#Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer
# qual deles é o maior.
from time import sleep
def maior(* num):
    cont = maior = 0
    print('\nAnalisando os valores passados... ')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0: #se nao tiver nenhum numero analisado
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'o maior valor informado foi {maior}')


maior(2, 9, 4, 7, 1, 5)
maior(1, 2)
maior(4, 7, 0)
maior(6)
maior()

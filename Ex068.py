#Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
print('=-'*20)
print('Jogo do par ou impar!')
print('=-'*20)
while True:
    n = int(input('Escolha um número: '))
    jogo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    comp = randint(1, 10)
    print('-'*20)
    print(f'Voce jogou {n} e o computador jogou {comp}')
    if (n + comp) % 2 == 0:
        if jogo in 'Pp':
            print('Voce ganhou!')
        else:
            print('Voce perdeu!')
            break
    else:
        if jogo in 'Ii':
            print('Voce ganhou!')
        else:
            print('Voce perdeu!')
            break
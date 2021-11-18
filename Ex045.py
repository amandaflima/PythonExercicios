from random import randint
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''suas opções:
[ 0 ] pedra
[ 1 ] papel
[ 2 ] tesoura''')
jogador = int(input('qual sua jogada? '))
print ('o computador jogou {}'.format(computador))
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VOCE GANHOU')
    elif jogador == 2:
        print('VOCE PERDEU')
    else:
        print('JOGADA INVALIDA'
              
elif computador == 1:
    if jogador == 0:
        print('VOCE PERDEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('V0CE GANHOU')
    else:
        print('JOGADA INVALIDA')

elif computador == 2:
    if jogador == 0:
        print('VOCE GANHOU')
    elif jogador == 1:
        print('VOCE PERDEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')


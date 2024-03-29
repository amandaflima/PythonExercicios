#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)}
ranking = []
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v}')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #o 1 coloca os valores em ordem, se fosse 0 iria colocar as chaves em ordem
print(ranking)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
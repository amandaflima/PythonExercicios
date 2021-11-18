#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep
num = randint(0,10)
print('Vou pensar em um número de 0 a 5, tente adivinhar!')
print('---------------------------------------------------------')

'''lista = [0,1,2,3,4,5]
num = random.choice(lista)'''


n = int(input('Qual número eu pensei? '))
print('Processando...')
sleep(1)

while num != n:
    n = int(input('Voce errou! Tente novamente: '))
print('Parabéns! Você acertou!')

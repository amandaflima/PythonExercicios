#jogo da adivinhação
#import random
from random import randint
from time import sleep
num = randint(0,5)
print('Vou pensar em um número de 0 a 5, tente adivinhar!')
print('---------------------------------------------------------')

'''lista = [0,1,2,3,4,5]
num = random.choice(lista)'''


n = int(input('Qual número eu pensei? '))
print('Processando...')
sleep(3)
if num == n:
    print('Parabéns! Você acertou!')
else:
    print('Você errou! O número é: {}'.format(num))

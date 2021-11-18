#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai
# perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint

lista = []
jogos = []
tot = 0
quant = int(input('Quantos jogos você quer fazer?'))
while tot < quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for c in range(0, quant):
    print(f'{c+1}º jogo:  {jogos[c]}')





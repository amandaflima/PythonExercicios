# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
sim = 0
nao = 0
for a in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}º pessoa: '.format(a)))
    if atual - ano >= 18:
        sim += 1
    else:
        nao += 1
print ('{} pessoas são maiores de idade e {} nao sao'.format(sim,nao))
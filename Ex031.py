#Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 parta viagens mais longas.

d = float(input('Qual a distancia da viagem? '))
if d <= 200:
    p = 0.5 * d
else:
    p = 0.45 * d
print ('o preço da passagem é {} '.format(p))
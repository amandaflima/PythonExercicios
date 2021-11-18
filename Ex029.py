#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
v = float(input('Qual é a velocidade do carro? '))
m=(v - 80) *7
if v >= 80:
    print ('Você foi multado! O limite é 80km/h. \n Sua multa vai custar {}'.format(m))

print('Tenha um bom dia! Dirija em segurança')
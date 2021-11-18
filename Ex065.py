#Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
s = 'S'
soma = media = cont = maior = menor = 0
while s in 'Ss':
    n = float(input('Digite um numero: '))
    s = str(input('Voce quer continua a digitar valores [S/N]')).strip().upper()[0]
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma/cont
print("a média é: {} e o maior é: {} e o menor é: {}".format(media, maior, menor))
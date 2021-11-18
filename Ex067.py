#Faça um programa que mostre a tabuada de vários números,
#um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
n = 0

while n >= 0:
    n = int(input('Digite um numero para exibir sua tabuada:'))
    cont = 1
    if n < 0:
        break
    while cont <= 10:
        print(f'{n} x {cont} = {n*cont}')
        cont += 1
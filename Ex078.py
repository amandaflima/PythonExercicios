#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista = []
maior = menor = 0
for c in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print(f'Voce digitou os valores: {lista}')
print(f'o maior valor é: {maior} e ele está na posição: ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i} - ', end='')
print(f'\no menor valor é: {menor} e ele está na posição: ', end='1')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}.. ', end='')



# Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

lista = []
todos = []
tot = maior = menor = 0
while True:
    lista.append(str(input('Digite o nome: ')))
    lista.append(float(input('Digite o peso: ')))
    if len(todos) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]
    todos.append(lista[:])
    lista.clear()
    tot += 1

    n = str(input('Voce quer cadastrar mais nomes?[S/N] ')).strip().upper()[0]
    if n in 'N':
        break
print(todos)
print(f'Foram cadastradas {tot} pessoas')
print(f'Foram cadastradas {len(todos)} pessoas')
print(f'O maior peso foi de:{maior} e é o peso de: ', end='')
for p in todos:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print(f'\nO menor peso foi de:{menor} e é o peso de ', end='')
for p in todos:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')





#Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    n = str(input('Voce quer adicionar mais um valor? [S/N]')).strip().upper()[0]
    if n in 'N':
        break
lista.sort(reverse=True)
print(f'Voce digitou {lista}, um total de {len(lista)} numeros')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 NAO faz parte da lista')

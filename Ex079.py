'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

lista = []
n = 'S'
while n in 'S':
    valor = int(input('Digite um valor: '))
    if valor in lista:
        print('esse valor ja foi digitado')
    else:
        lista.append(valor)
    n = str(input('Voce quer adicionar mais um valor? [S/N]')).strip().upper()[0]
lista.sort()
print(f'Voce digitou {lista}')


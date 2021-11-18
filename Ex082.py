#Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores
# ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
lista = []
listapar = []
listaimpar = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
    n = str(input('Voce quer adicionar mais um valor? [S/N]')).strip().upper()[0]
    if n in 'N':
        break


print(f'Voce digitou {lista}')
print(f'A lista de par é {listapar}')
print(f'A lista de impar é {listaimpar}')
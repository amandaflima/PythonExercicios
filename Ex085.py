#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
# lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
lista = [[], []]
valor = 0
for cont in range(1, 8):
    valor = int(input(f'Digite o {cont}º valor'))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
num[0].sort
num[1].sort
print(f'Todos os valores: {lista}')
print(f'Todos os valores pares: {lista[0]}')
print(f'Todos os valores impares: {lista[1]}')
# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados
# cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média
pessoa = {}
galera = []
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Digite o sexo correto')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar?[S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite apenas sim ou não')
    if resp in 'N':
        break
media = soma / len(galera)
print(galera)
print(f'Foram cadastradas {len(galera)} pessoas')
print(f'A média das idades é de {media:5.2f}')
print('as mulheres sao: ', end='')
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ', end='')
print('\nAs pessoas acima da media sao: ', end='')
for p in galera:
    if p['idade'] > media:
        print(f'{p["nome"]} ', end='')


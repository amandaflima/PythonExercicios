#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
cont = 0
id = 0
homemidade = 0
nomevelho = ''
for c in range(1, 5):
    nome = str(input('NOME: '))
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).upper()

    if sexo in 'Ff':
        if idade < 20:
            id += 1
    elif sexo in 'Mm' and c == 1:
        homemidade = idade
        nomevelho = nome
    elif sexo in 'Mm' and idade > homemidade:
        homemidade = idade
        nomevelho = nome

    else:
        print('sexo invalido')

    print('-'*15)
    cont += idade
media = cont / 4
print('a idade media do grupo é {}'.format(media))
print('o homem mais velho tem {}'.format(nomevelho))
print('{} mulheres tem menos que 20 anos'.format(id))
#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
#No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

alunos = []
while True:
    nome = str(input('Qual o nome do aluno? '))
    nota1 = float(input('Qual é a primeira nota do aluno? '))
    nota2 = float(input('Qual é a segunda nota do aluno? '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? '))
    if resp in 'Nn':
        break
print(alunos)
print(f'{"No.":<4}{"nome":<10}{"media":>8}')
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:8.1f}')


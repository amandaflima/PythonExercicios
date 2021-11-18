# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno = {}
aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['média'] = float(input('Digite a média: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] ='Recuperação'
for k, v in aluno.items():
    print(f'{k} é {v}')
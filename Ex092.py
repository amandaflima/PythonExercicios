#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
# em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
# contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar
from datetime import datetime
trabalho = {}
trabalho['nome'] = str(input('Digite o nome: '))
data = int(input('Digite o ano de nascimento: '))
trabalho['idade'] = datetime.now().year - data
trabalho['carteira'] = int(input('Carteira de trabalho (0 não tem): '))
if trabalho['carteira'] != 0:
    trabalho['contratação'] = int(input('Qual o ano de contratação? '))
    trabalho['salario'] = float(input('Qual o salario? '))
for k, v in trabalho.items():
    print(f'{k} tem o valor {v}')
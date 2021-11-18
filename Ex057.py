#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
n = str(input('Digite o sexo [M/F]')).strip().upper()[0] #esse [0] faz com que ele pegue só a primeira letra e se ele digitar Masculino funciona
while n not in 'MmFf':
    n = str(input('Dado invalido, por favor insira o sexo [M/F]')).strip().upper()[0]
print('sexo {} registrado com sucesso'.format(n))
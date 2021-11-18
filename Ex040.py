#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADOatingida
n1 = int(input('digite a primeira nota: '))
n2 = int(input('digite a segunda nota: '))
m = (n1 + n2) / 2
if m >= 7:
    print('APROVADO COM MEDIA {}'.format(m))
elif m < 5:
    print('REPROVADO COM MEDIA {}'.format(m))
else:
    print('RECUPERAÇÃO COM MEDIA {}'.format(m))
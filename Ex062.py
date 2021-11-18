#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.


a1 = int(input('Qual o primeiro termo da PA? '))
r = int(input('Qual a razão da PA? '))
termo = a1
cont = 1
total = 0
mais = 10 #valor inicial que começa
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} '.format(termo), end='')
        termo += r
        cont += 1
    mais = int(input('Quantos termos mais voce quer mostrar? '))



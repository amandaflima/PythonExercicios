#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

n = float(input('qual o seu salário? '))
if n > 1250:
    a = 1.1 * n
else:
    a = 1.15 * n
print('O salário com aumento é: {}'.format(a))


''' Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

v = float(input('Qual o valor da casa? '))
s = float(input('qual o seu salario? '))
a = float(input('em quantos anos quer pagar? '))
p = v / (a * 12)
if p <= 0.3 * s:
    print('empréstimo aprovado com parcelas de: {:.2f} '.format(p))
else:
    print('empréstimo negado ')
'''Escreva um programa em Python que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
 1 para binário, 2 para octal e 3 para hexadecimal.'''

n = int(input('digite um numero: '))
print('''Escolha uma para converter: 
[ 1 ] converter para binário
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal''')
op = int(input('sua opção: '))
if op == 1:
    print('convertido para binário é: {}'.format(bin(n)))
elif op == 2:
    print('convertido para octal é: {}'.format(oct(n)))
elif op == 3:
    print('convertido para hexadecimal é: {}'.format(hex(n)))
else:
    print('isso não é uma opção válida')

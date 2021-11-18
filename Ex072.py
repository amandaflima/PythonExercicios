#Crie um programa que tenha uma Tupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
cont = ('zero', 'um', 'dois', 'tres', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'catorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if 0 <= n <= 20:
                print(f'Você digitou o número {cont[n]}')  # cont na posição n para exibir o elemento por extenso
                tent = str(input('Quer digitar mais algum valor? [S/N]')).strip().upper()[0]
                if tent == 'N':
                        break
        else:
                print('tente novamente. ', end='')

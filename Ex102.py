#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o
# primeiro que indique o número a calcular e outro chamado show, que será um valor lógico
# (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show == 'S':
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return f


n = int(input('Digite um numero: '))
show = str(input('Voce quer mostrar o processo do fatorial? [S/N] ')).upper()[0]
print(fatorial(n))

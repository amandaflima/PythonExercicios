'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
tot = totcol = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um numero para [{l},{c}]: '))
        tot += matriz[l][c]
        if c == 2:
            totcol += matriz[l][c]
        if l == 1:
            if matriz[l][c] > maior:
                maior = matriz[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='') #isso :^5 centraliza
    print()
print(f'A soma é: {tot}')
print(f'A soma da 3 coluna é: {totcol}')
print(f'O maior da segunda linha é: {maior}')
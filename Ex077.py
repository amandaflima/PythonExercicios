#Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'CURSO', 'GRATIS')
for n in palavras:
    print (f'\nPara a palavra {n} temos ', end='')
    for letra in n:
        if letra in 'AEIOU':
            print(letra, end='')
#sorteando uma ordem na lista
import random
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1,a2,a3,a4]
random.shuffle(lista)
print('a ordem é ')
print(lista)
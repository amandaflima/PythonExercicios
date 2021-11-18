#Desenvolva um programa que leia quatro valores pelo teclado
# e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

num = (int(input('Digite um numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite o ultimo numero numero: ')))
print(f'Voce digitou o número 9 {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 está na {num.index(3)+1} posição')
print('Os números pares são: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')


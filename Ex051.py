# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
a1 = int(input('Qual o primeiro termo da PA? '))
r = int(input('Qual a razão da PA? '))
for n in range(0, 10):
    t = a1 + (n*r)
    print('{}'.format(t), end=' ')
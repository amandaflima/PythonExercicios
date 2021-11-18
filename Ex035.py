# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('-=-'*10)
print('Analisador de triângulos')
print('-=-'*10)
a = float(input('Digite o primeiro lado: '))
b = float(input('Digite o segundo lado: '))
c = float(input('Digite o terceiro lado: '))
if a < b + c and b < a + c and c < a + b:
    print('os valores podem formar um triangulo!')
else:
    print('os valores não formam triangulo')
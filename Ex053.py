#Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços.
a = str(input('digite uma frase: ')).strip().upper()
palavras = a.split() #separa a frase em palavras
junto = ''.join(palavras) #junta sem espaços
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if junto == inverso:
    print('É PALINDROMO')
else:
    print('não é palindromo')


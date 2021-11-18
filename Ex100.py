#Faça um programa que tenha uma lista chamada números e
# duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los
# dentro da lista e a segunda função vai mostrar a soma
# entre todos os valores pares sorteados pela função anterior.
from random import randint
def sorteia(lista):
    #sorteio de 5 num e coloca na lista
    for cont in range(0,5):
        lista.append(randint(1, 10))
def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(soma)
    #mostra a soma entre os valores pares sorteados
numeros = []
sorteia(numeros)
print(numeros)
somaPar(numeros)



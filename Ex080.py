#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]: #se ele é o primeiro ou maior que o utimo
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista): #enquanto pos for menor que o tamanho da lista
            if n <= lista[pos]:
                lista.insert(pos, n) #coloca pos na posição de n
                break
            pos += 1
print(f'Os valores digitados em ordem sao {lista}')





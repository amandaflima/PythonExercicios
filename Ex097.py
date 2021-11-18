#Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma
# mensagem com tamanho adaptável.

def escreva(msg):
    print('-' * (len(msg)+4))
    print(f'  {msg}')
    print('-' * (len(msg)+4))


escreva(msg = str(input('Digite um texto: ')))
#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
#diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
import moeda

preco = float(input('Digite um preço: '))
print(f'O dobro de {preco} é {moeda.dobro(preco)}')
print(f'A metade de {preco} é {moeda.metade(preco)}')
print(f'Aumentando 10% temos {moeda.aumentar(preco)}')
print(f'Diminuindo 10% temos {moeda.diminuir(preco)}')

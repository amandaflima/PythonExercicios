#Adapte o código do desafio #107, criando uma função adicional chamada moeda()
#que consiga mostrar os números como um valor monetário formatado.
import moeda

preco = float(input('Digite um preço: '))
print(f'O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
print(f'Aumentando 10% temos {moeda.aumentar(preco)}')
print(f'Diminuindo 10% temos {moeda.diminuir(preco)}')
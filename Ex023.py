num = int(input('Digite um número: '))
u = num % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000
print('unidade: {} \n dezena {} \ncentena {} \nmilhar {}'.format(u,d,c,m))
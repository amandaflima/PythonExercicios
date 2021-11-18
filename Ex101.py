#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
# nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO,
# OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(nasc):
    from datetime import date #declarar dentro para economizar memória
    atual = date.today().year
    id = atual - nasc
    if id > 18:
        return f'Com {id} anos : VOTO OBRIGATÓRIO'
    elif id >= 16:
        return f'Com {id} anos : VOTO OPICIONAL'
    else:
        return f'Com {id} anos : VOTO NEGADO'


nasc = int(input('Em que ano voce nasceu? '))
print(voto(nasc))
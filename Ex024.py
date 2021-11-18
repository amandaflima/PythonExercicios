#programa que leia o nome de uma cidade e diga se começa ou não com "santo"
cidade = str(input('Em qual cidade voce nasceu? ')).strip().capitalize()
print(cidade[:5] =='Santo')

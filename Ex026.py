frase = str(input('escreva uma frase: ')).strip()
print('a letra A aparece {} vezes'.format(frase.lower().count('a')))
print ('a primeira letra A aparece na {} posição'.format(frase.lower().find('a')+1))
print ('a ultima letra A aparece na {} posição'.format(frase.lower().rfind('a')+1))
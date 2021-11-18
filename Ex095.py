'''Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.'''

jogador = {}
jogos = []
lista = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Qual o nome do jogador? '))
    partidas = int(input('Quantas partidas ele jogou? '))
    for c in range(0, partidas):
        jogos.append(int(input(f'Quantos gols ele fez na {c+1}º partida?')))
    jogador['gols'] = jogos[:]
    jogador['total'] = sum(jogos)
    lista.append(jogador.copy())
    resp = str(input('Quer continuar?[S/N]')).upper()[0]
    if resp != 'S' and resp != 'N':
        print('ERRO! Digite apenas sim ou não')
    if resp == 'N':
        break


print(lista)

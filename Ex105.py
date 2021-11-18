'''Faça um programa que tenha uma função notas() que pode receber várias notas
# de alunos e vai retornar um dicionário com as seguintes informações:

– Quantidade de notas
– A maior
– A menor nota
– A média da turma
– A situação (opcional)'''

def notas(*n, sit=True):
   """
   -> Função para analisar notas e situações de vários alunos
   :param n: uma ou mais notas dos alunos (aceita várias)
   :param sit: valor opcional, indicando se deve ou não adicionar a situação
   :return: dicinarios com varias informações sobre a situação
   """
   r = {}
   r['total'] = len(n)
   r['maior'] = max(n)
   r['menor'] = min(n)
   r['media'] = sum(n)/len(n)
   if sit:
      if r['media'] >= 7:
         r['situação'] = 'boa'
      elif r['media'] >= 5:
         r['situação'] = 'razoavel'
      else:
         r['situação'] = 'ruim'

   return r


resp = notas(5.5, 2.5, 1.5)
print(resp)
help(notas)




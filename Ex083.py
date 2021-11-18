#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisrênteses abertos e fechados na ordear se a expressão passada está com os pam correta

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()  #ele remove o do inicio ou seja o par dele
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão esta valida')
else:
    print('sua expressao esta invalida')
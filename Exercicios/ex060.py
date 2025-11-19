#Crie um programa onde o utilizador
#possa inserir uma equação matemática
#que use parênteses. O programa deverá
#analisar a equação e dizer se a equação
#tem os parênteses corretos ou se está
#errado.

#((a+b)-c(c/d) ((a+b)-c(c/d))

expressao=input(int('Digite uma expressão matemática: '))

if expressao.count('(')==expressao.count(')'):
    print('A expressão está correta.')
else:
    print('A expressão não está correta.')
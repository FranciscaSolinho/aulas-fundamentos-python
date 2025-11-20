#json
#javascript object notation

turma=[]
qtd_alunos=5

for c in range(qtd_alunos):

    aluno= dict() # ou {}

    aluno['Nome']=input(f'Digite o nome do {c+1}º aluno: ')
    aluno['Média']=float(input('Digite a média: '))
    #aluno['Média']=float(input('Digite a média do(a) {aluno['Nome']}: '))

    #Situação com Operador Ternário:
    aluno['Situação']='Aprovado' if aluno['Média']>=9.5 else 'Reprovado'

    #Situação com IF normal:
    #if aluno['Média']>9.5:
        #aluno['Situação']='Aprovado'
    #else:
        #aluno['Situação']='Reprovado'

    turma.append(aluno.copy())

print(turma)
    #print(aluno) #.values))
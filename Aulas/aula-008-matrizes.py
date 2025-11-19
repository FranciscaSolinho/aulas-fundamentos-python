aluno1=['Telmo', 14]
aluno2=['Solinho', 17]
aluno3=['Pedro', 16]
aluno4=['Leticia', 15]

turma=list()
turma.append(aluno1)
turma.append(aluno2)
turma.append(aluno3)
turma.append(aluno4)

#print(turma)

#aluno1[0]='Alexandra'
#aluno1[1]=18

#print(turma)

#Valores primitivos: boolean, int, char, float
#[:] --> Significa do inicio ao fim de um append
#stack - copia de duas cenas que qd alterado não altera as restantes copias
#heap - 1 unico que pode ser alterado por quem tiver o ficheiro

for aluno in turma:
    #print(f'O/A aluno/a {aluno[0]} tem uma média de {aluno[1]} valores.')
    # OU
    for valor in aluno:
        print(valor)

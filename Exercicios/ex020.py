nome=input('Digite o seu nome:').strip()

print(nome.upper()) #Nome com todas as letras maiúsculas
print(nome.lower()) #Nome com todas as letras minúsculas
print(len(nome.replace(' ',''))) #Quantidade de letras sem espaços
print(len(nome[0:nome.find(' ')])) #Quantas letras tem o primeiro nome

#Correção:
qtd_espacos=nome.count(' ')
print(len(nome)-qtd_espacos)
pEspaco=nome.find(' ') #Encontra o indice do primeiro espaço
print(nome[:pEspaco]) #Mostra so a primeira palavra antes do primeiro espaço

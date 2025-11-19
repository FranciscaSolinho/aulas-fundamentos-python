frase=input('Digite uma frase:')

print(frase.count('A')) #Quantas vezes aparece a letra "A"
print(frase.find('A')) #Em que posição aparece a primeira vez
print(int(len(frase))-int(frase[::-1].find('A'))) #Em que posição aparece a última vez

#Correção
qtd_a=frase.count('A')
print(f'O A aparece {qtd_a} vezes.')

p_posicao=frase.find('A')
print(f'Aparece pela primeira vez na posição {p_posicao+1}.')

u_posicao=frase.rfind('A')
print(f'Aparece pela ultima vez na posição {u_posicao+1}.')
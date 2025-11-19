string = 'Python é poderoso'

#Fatiamento de string/String slicer
print(string[7]) # é
print(string[-1]) # último caracter
print(string[:6]) # Python
print(string[9:]) # Poderoso
print((string[::2])) # Do inicio ao fim de 2 em 2
print(string[::-1]) # Mostra a string ao contrário

#Análise de string/String analysis

print(len(string)) # Tamanho da string (lenght)
print(string.count('o')) # Quantas vezes aparece a letra introduzida, neste caso o "o"
print('Phyton' in string) # Devolve true ou false, conforme a palavra inserida
print(string.find('é')) # Devolve a posição do solicitado
print(string.find('Olé')) # Devolve "-1" com a tradução de "não encontrou"
print(string.startswith('Phyton')) # Devolve true ou false (procura o que foi inserido)
print(string.endswith('Fraquinho')) # Devolve true ou false (procura o que foi inserido)

#Transformação de string/String transfiguration

string = input('Digite uma frase:')

print(len(string))
print(len(string.strip())) # Tira espaços "inadvertidos" de ambos os lados (não no meio)
print(len(string.rstrip())) # Só tira os espaços à direita
print(string.lower()) # Coloca tudo em minúsculas
print(string.upper()) # Coloca tudo em maiúsculas
print(len(string.replace(' ',''))) # Tira o "old" para substituir pelo "new" (neste caso tirei espaços)

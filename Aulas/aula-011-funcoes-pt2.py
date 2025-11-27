#nome=print('Digite o seu nome: ') #assim n funciona teria q tirar "nome="
#nome=input('Digite o seu nome: ')# função que recebe o nome gerado/ a função input devolve uma string

#EXEMPLO A:

#def soma (numero1: int, numero2: int):
    #s=numero1+numero2
   #print(f'A soma deu {s}')
    #return s

#resultado=soma(numero1:5, numero2:5)

#EXEMPLO B:

def soma_numeros (lista: list) -> int:
    soma=0
    for numero in lista:
        soma+=numero
    return soma

notas=[20,20,20,20]
media=soma_numeros(notas)/len(notas)
print(media)
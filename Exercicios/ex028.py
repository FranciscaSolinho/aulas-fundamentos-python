print('--- Jogo da Adivinha v1.0 ---')

import random
rnumber = random.randint(0,7)

print('Vou escolher um número entre 0 e 7...Tenta adivinhar.')
numero_recebido = int(input('Digita um número: '))

if numero_recebido == rnumber:
    print('Parabéns! Acertou!')
else:
    print(f'Temos pena...Perdeste. Eu pensei em {rnumber} e tu disseste {numero_recebido}.')
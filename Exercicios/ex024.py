print('--Radar de Velocidade--')

velocidade=int(input('Introduza valor da velocidade--> '))
limite_velocidade=80
multa=100
multa_extra=(velocidade-limite_velocidade)*7
multa_total=multa+multa_extra

if velocidade>limite_velocidade:
    print('Multado')
    print(f'Pagamento: {multa_total:.2f}€')#:.2f->para mostrar com 2 casas decimais
else:
    print('Não Multado.')







print('~*º~*º~*º Calculadora - IMC (Índice de Massa Corporal) º*~º*~º*~')
# Fórmula do IMC = peso / (altura**2)


peso=float(input('Digite o seu peso(kg)--> '))
altura=float(input('Digite a sua altura(cm)--> '))/100
imc=peso/(altura**2)

if imc <18.5:
    print(f'Abaixo do peso normal. IMC: {imc:.2f}')
    print('Not bad mas vá comer alguma coisa sff u-U')
elif imc <24.9:
    print(f'Peso normal. IMC: {imc:.2f}')
    print('Parabénssssss ^-^')
elif imc <29.9:
    print(f'Sobrepeso. IMC: {imc:.2f}')
    print('Ta "fortezinho/a" :)')
elif imc <34.9:
    print(f'Obesidade Grau I. IMC: {imc:.2f}')
    print('Então??? Já tá obeso!!! D:')
elif imc <39.9:
    print(f'Obesidade Grau II. IMC: {imc:.2f}')
    print('Se está na obesidade grau II é porque escolheu este estilo de vida.')
elif imc >40:
    print(f'Obesidade Grau III (Obesidade Mórbida). IMC: {imc:.2f}')
    print('Já escolheu o seu caixão? Aproveite já a nossa promoção na Funerária Fatty-senpai')




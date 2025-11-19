kms = int(input('quantos km foram feitos? '))
dias = int(input('quantos dias foram utilizados? '))

custo_km = kms * 0.456
custo_dia = dias * 60
total = custo_km + custo_dia

print ('O total a pagar será ', total)

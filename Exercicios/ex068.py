pessoas=[]
qtd_pessoas=0
soma_idades=0
qtd_mulheres=0

while True:
    dados=dict()
    dados['nome']=input('Digite o nome: ') #não limpamos esta info #(1*) .strip se usar a info que escrevi no final
    while True:
        dados['sexo']=input('Digite o sexo [m/f]: ')#limpamos esta info
        if dados['sexo'] != 'm' and dados['sexo'] != 'f':
            print('Introduza um sexo válido.')
        else:
            break
    if dados['sexo']=='f':
        qtd_mulheres+=1

    media_idades=round(soma_idades/qtd_pessoas,2)
    qtd_homens_acima_media=0

    for pessoa in pessoas:
        if pessoa['sexo']=='m':
            if pessoa['idade']>media_idades:
                qtd_homens_acima_media+=1

    print('------------------------------')
    print('Informações:')
    print(f'--> Foram registadas {qtd_pessoas} pessoas.')
    print(f'--> A média de idade é {media_idades} anos.')
    print(f'--> Foram registadas {qtd_mulheres} mulheres.')
    print(f'--> Foram registados {qtd_homens_acima_media} homens com idade acima da média.')


    dados['idade']=int(input('Digite a idade: '))
    soma_idades+=dados['idade']
    pessoas.append(dados.copy())
    qtd_pessoas+=1
    print(pessoas)


    #outra forma de fazer este exercício(1*):
    #pessoas.append(dados.copy())
    #dados.clear() ---> apaga o dicionário
    #opcao=input('Digite "sim" para terminar---> ').strip().lower()
    #if opcao=='sim':
        #break
    #print(pessoas)





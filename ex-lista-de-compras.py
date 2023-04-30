lista_de_compras = []

while True:
    print('----------------------------------------')
    print('Selecione uma opção')
    opcoes = input('[i]nserir  [a]pagar  [t]apgar-tudo  [l]istar  [s]air: ').lower()
    
    if opcoes == 'i':
        item = input('Digite um item para lista: ')
        lista_de_compras.append(item)

    elif opcoes == 's':
        print('---------------SAINDO---------------')
        break

    elif opcoes == 'a':
        if len(lista_de_compras) == 0:
            print('Não tem nada na lista para apagar')
            continue
        indice = int(input('Qual indice deseja apagar? '))
        del lista_de_compras[indice]

    elif opcoes == 't':
        if len(lista_de_compras) == 0:
            print('Não tem nada na lista para apagar')
            continue
        del lista_de_compras
        print('Apagou Tudo')
        lista_de_compras = []
    
    elif opcoes == 'l':
        if len(lista_de_compras) == 0:
            print('Não tem nada na lista')
            continue
        for objeto in enumerate(lista_de_compras):
            indice, nome = objeto
            print(indice, nome)
    else:
        print('Erro...')

print('FIM....')
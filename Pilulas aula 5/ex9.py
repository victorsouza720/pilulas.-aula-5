def calcularmedia(prod,quali,pont):
    return(prod + quali + pont)/3

def classificar (media):
    if media >= 8:
        return ' excelente'
    elif media >= 6:
        return ' bom' 
    else:
        return 'critico'
def avaliar_funcionarios():
    total = 0
    exc = 0
    bom = 0
    crit = 0
    melhornome = ' '
    melhormedia = -1

    while True:
        nome = input ('nome: ')
        if nome == 'fim':
            break
        prod = float(input('produtividade: '))
        quali = float(input('qualidade: '))
        pont = float(input('pontualidade: '))
        
        media = calcularmedia(prod,quali,pont)
        categoria = classificar(media)
        print(f'{nome}, media {media}, {categoria} ')
        
        total += 1
        if categoria =='excelente':
            exc += 1
        elif categoria == 'bom':
            bom += 1
        else:
            crit += 1

        if media > melhormedia:
            melhormedia = media
            melhornome = nome
    if total == 0 :
        print ('nada para calcular')
        return
    print("-" * 50)
    print('relatorio')
    print("-" * 50)
    print(f'total de func: {total}')
    print(f'excelente: {exc}')
    print(f'bom: {bom}')
    print(f'critico: {crit}')
    print(f'melhor func: {melhornome}')
    print(f'melhor func media{melhormedia}')

avaliar_funcionarios()

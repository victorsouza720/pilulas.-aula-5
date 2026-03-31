def Menu():
    while True:
        op = int(input('MENU\n1 - Soma \n2 - Media \n3 - Sair\nOpção'))
        if op == 3:
            break

        n1 = float(input('N1: '))
        n2 = float(input('N2: '))
        if op == 1:
            print (f'soma {n1} + {n2} ={n1+n2} ')
        elif op == 2:
            print(f'Media de {n1} e {n2} = {(n1+ n2)/2}')
        else:
            print ('Opção errada')
    
Menu()

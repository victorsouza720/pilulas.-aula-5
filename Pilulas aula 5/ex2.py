def simularcrecimento(populacao, taxa , limite):
    anos = 0
    while populacao <= limite:
        populacao = populacao * (1 + taxa)
        anos += 1
        return anos

#main
p = float(input('população inicial: '))
t = float(input('Taxa(%): '))/100
l = float(input('limite: '))

print(f'Anos = {simularcrecimento(p,t,l )}')


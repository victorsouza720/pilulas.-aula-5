def validarsenha (senha):
    if len (senha)< 8:
        return 'Senha invalida, muito curta'
    
    temnumero = False
    temmaiuscula = False

    for c in senha:
        if c == ' ':
            return 'Senha invalida, nao pode conter espaço.'
        
        if c >= '0' and c <=  '9':
            temnumero = True
        
        if c >= 'A' and c <= 'Z':
            temmaiuscula = True
    
    if not temnumero:
        return 'Senha invalida,nao tem numero '
    
    if not temmaiuscula:
        return 'Senha invalida,nao tem maiuscula '
    
    return 'senha valida'


#main
senha = input ("Digite a sua senha:")
print (validarsenha(senha))

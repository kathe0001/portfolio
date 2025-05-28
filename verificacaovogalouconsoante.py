def verificar_vogal_consoante(letra):
    letra = letra.lower()
    vogais = 'aeiou'
    
    if letra.isalpha() and len(letra) == 1:
        if letra in vogais:
            return "A letra '{}' é uma vogal.".format(letra)
        else:
            return "A letra '{}' é uma consoante.".format(letra)
    else:
        return "Por favor, insira apenas uma letra"
    
    resultado = verificar_vogal_consoante('A')
    print(resultado)
    
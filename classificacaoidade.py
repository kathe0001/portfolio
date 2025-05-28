def classificar_idade(idade):
    if idade < 12:
        return 'criança'
    elif 12 <= idade < 18:
        return 'adolescente'
    elif 18 <= idade < 30:
        return 'jovem'
    else:
        return 'adulto'

# Exemplo de uso
idades = [5, 13, 25, 45, 10, 17, 30]
classificacoes = {idade: classificar_idade(idade) for idade in idades}

for idade, classificacao in classificacoes.items():
    print(f'A idade {idade} é classificada como: {classificacao}')

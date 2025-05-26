def verificar_aprovacao(nota1 + nota2 + nota3):
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado" 
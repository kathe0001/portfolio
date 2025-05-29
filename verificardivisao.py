def verificar_divisibilidade(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return True
    else:
        return False

# Exemplo de uso
numero = int(input("Digite um número: "))
if verificar_divisibilidade(numero):
    print(f"O número {numero} é divisível por 3 e 5.")
else:
    print(f"O número {numero} não é divisível por 3 e 5.")

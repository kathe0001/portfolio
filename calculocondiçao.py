# Função para calcular o desconto
def calcular_desconto(valor_compra):
    if valor_compra > 100:
        desconto = valor_compra * 0.10  # 10% de desconto
        valor_final = valor_compra - desconto
        return valor_final, desconto
    else:
        return valor_compra, 0  # Sem desconto

# Exemplo de uso
valor_compra = float(input("Digite o valor da compra: R$ "))
valor_final, desconto = calcular_desconto(valor_compra)

print(f"Valor original: R$ {valor_compra:.2f}")
if desconto > 0:
    print(f"Desconto aplicado: R$ {desconto:.2f}")
print(f"Valor final a pagar: R$ {valor_final:.2f}")

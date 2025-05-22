print("Bem vindo a nossa cafeteria")

valor_cafe = float(input("Qual o valor de um café? R$"))

# Pergunta quantos cafés o usuário quer comprar

quantidade = int(input("Quantos cafés você quer comprar?"))

# Calcula o total pagar
total = valor_cafe * quantidade

# Exibir resultado
print(f"você deve pagar R$ {total:.2f}")

# Função para verificar se o aluno foi aprovado
def verificar_aprovacao(notas):
    media = sum(notas) / len(notas)
    if media >= 7.0:
        return "Aprovado"
    else:
        return "Reprovado"

# Entrada de notas do aluno
notas = []
num_notas = int(input("Digite o número de notas: "))

for i in range(num_notas):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)

# Verificando a aprovação
resultado = verificar_aprovacao(notas)
print(f"O aluno foi: {resultado}")

    

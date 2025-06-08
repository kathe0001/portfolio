letra = input("Digite uma letra: ").lower()

if len(letra) != 1 or not letra.isalpha():
    print("Por favor, digite apenas uma letra do alfabeto.")
else:
    if letra in "aeiou":
        print(f"A letra '{letra}' é uma vogal.")
    else:
        print(f"A letra '{letra}' é uma consoante.")

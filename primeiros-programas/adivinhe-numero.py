numero_secreto = 7  # Você pode escolher qualquer número
tentativas = 0

while tentativas < numero_secreto:
    chute = int(input("Tente adivinhar o número secreto: "))
    tentativas += 1
    if chute == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break
    else:
        print("Errou! Tente novamente.")
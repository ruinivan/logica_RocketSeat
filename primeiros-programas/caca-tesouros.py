def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(' | '.join(linha))
    print()

tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
tesouro_linha = 1
tesouro_coluna = 2
tentativas = 5

for tentativa in range(1, tentativas + 1):
    print(f"Tentativa {tentativa} de {tentativas}")
    exibir_tabuleiro(tabuleiro)
    try:
        linha = int(input("Chute a linha (0-2): "))
        coluna = int(input("Chute a coluna (0-2): "))
    except ValueError:
        print("Digite apenas números inteiros!")
        continue

    if not (0 <= linha <= 2 and 0 <= coluna <= 2):
        print("Posição inválida! Tente valores entre 0 e 2.")
        continue

    if tabuleiro[linha][coluna] != ' ':
        print("Você já tentou esse local!")
        continue

    if linha == tesouro_linha and coluna == tesouro_coluna:
        tabuleiro[linha][coluna] = '💎'
        exibir_tabuleiro(tabuleiro)
        print("Parabéns! Você encontrou o tesouro!")
        break
    else:
        tabuleiro[linha][coluna] = 'X'
        print("Nada aqui...")

else:
    print("Suas tentativas acabaram!")
    tabuleiro[tesouro_linha][tesouro_coluna] = '💎'
    exibir_tabuleiro(tabuleiro)
    print(f"O tesouro estava na linha {tesouro_linha}, coluna {tesouro_coluna}!")
import os

tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
jogador = 'X'

def exibirTabuleiro():
    print()
    for linha in tabuleiro:
        print('|'.join(linha))
        print('-' * 5)
    print()

def jogada(linha, coluna):
    if (
        not 0 <= linha <= 2 or 
        not 0 <= coluna <= 2 or
        tabuleiro[linha][coluna] == ' '
    ):
        tabuleiro[linha][coluna] = jogador
        return 'O' if jogador == 'X' else 'X'
    else:
        print('Jogada invalida, jogue dnv')
        return jogador

def temGanhador():
    for linha in range(3):
        if (
            tabuleiro[linha][0] != ' ' and
            tabuleiro[linha][0] == tabuleiro[linha][1] and 
            tabuleiro[linha][0] == tabuleiro[linha][2]
        ):
            return True
    for coluna in range(3):
        if (
            tabuleiro[0][coluna] != ' ' and
            tabuleiro[0][coluna] == tabuleiro[1][coluna] and 
            tabuleiro[0][coluna] == tabuleiro[2][coluna]
        ):
            return True
    if(tabuleiro[1][1] != ' 'and
        ((tabuleiro[0][0] == tabuleiro[1][1]and
         tabuleiro[0][0] == tabuleiro[2][2]) or
        (tabuleiro[0][2] == tabuleiro[1][1] and
         tabuleiro[1][1] == tabuleiro[2][0]))
    ):
        return True
    return False

def temEmpate():
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == ' ':
                return False
    return True

while True:
    os.system('cls')
    exibirTabuleiro()
    if temGanhador():
        print(f'O jogador {'O' if jogador == 'X' else 'X'} GANHOU!')
        break
    if temEmpate():
        print('Empatou!')
        break
    print(f'jogador da vez: {jogador}')
    try:
        linha = int(input('Digite a linha: '))
        coluna = int(input('Digite a coluna: '))
        jogador = jogada(linha, coluna)
    except (ValueError, IndexError):
        print('Digite um valor número inteiro entre 0 e 2')

perguntas = [
    ["Qual a linguagem principal do backend web? (python/js/java)", "python"],
    ["Qual comando imprime algo na tela em Python?", "print"],
    ["Qual estrutura armazena vários valores? (lista/dicionario)", "lista"],
    ["Como se chama a repetição de código? (loop/if)", "loop"]
]

acertos = 0

for pergunta, resposta_correta in perguntas:
    resposta = input(pergunta + " ").lower()
    if resposta == resposta_correta:
        print("Acertou!")
        acertos += 1
    else:
        print("Errou!")

print(f"Você acertou {acertos} de {len(perguntas)} perguntas!")
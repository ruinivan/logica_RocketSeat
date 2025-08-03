perguntas = [['Seu animal gosta de banana? ', 'Macaco'], ['É laranja? ', 'tigre']]
acertou = False

while not acertou :
    for index in perguntas:
        r = input(index[0])
        if r.lower() == 's':
            print(f'Seu animal é o {index[1]}')
            acertou = True
            break
    if not acertou:
        animal = input('Desisto! Qual era o seu animal? ')
        pergunta = input('Qual pergunta eu poderia ter feito? ')
        perguntas.append([pergunta, animal])
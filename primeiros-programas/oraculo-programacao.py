print('Olá, eu sou o Oraculo da Porgramação')
print('O que posso te ensinar hoje?')
comando = input('Digite um comando: ')

match comando:
    case 'oi' | 'ola':
        print('Oi, como você vai?')
    case 'tchau' | 'sair' | 'fim':
        print('Tchau!')
    case 'piada':
        print('Sabe qual é o padroeiro das pessoas que trabalham com TI? O São Login')
    case 'clima':
        print('Tá muito quente!')
    case _:
        print('Desculpe! Não entendi o comando')
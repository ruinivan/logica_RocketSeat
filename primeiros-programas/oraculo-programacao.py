print('Olá, eu sou o Oráculo da Sabedoria Python!')
print('Sobre qual assunto de programação você quer saber?')
print('Exemplos: variáveis, funções, listas, dicionários, loops')

assunto = input('Digite um assunto: ').lower()

match assunto:
    case 'variáveis' | 'variaveis':
        print('Variáveis são usadas para armazenar valores. Exemplo: x = 10')
    case 'funções' | 'funcao' | 'função' | 'funcoes':
        print('Funções são blocos de código reutilizáveis. Exemplo: def minha_funcao():')
    case 'listas':
        print('Listas armazenam vários valores. Exemplo: minha_lista = [1, 2, 3]')
    case 'dicionários' | 'dicionarios':
        print('Dicionários armazenam pares chave-valor. Exemplo: meu_dict = {"nome": "Ana"}')
    case 'loops' | 'laços' | 'lacos':
        print('Loops repetem ações. Exemplo: for i in range(5): print(i)')
    case _:
        print('Desculpe! Ainda estou aprendendo sobre esse assunto.')
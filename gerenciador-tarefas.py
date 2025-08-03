import os

tarefas = []

def adicionar_tarefas(tarefa):
    tarefas.append((tarefa, 'pendente'))
    print()
    print(f'Tarefa {tarefa} adicionada com sucesso!')
    print()

def listar_tarefas():
    global tarefas
    if not tarefas:
        print('A lista está vazia')
        return
    for t in tarefas:
        print(f'{t[0]} - {t[1]}')
    print()
        
def concluir_tarefa(tarefa):
    global tarefas
    tarefas = [(t[0], 'concluída') if t[0].lower() == tarefa.lower() else t for t in tarefas]

def remover_tarefa(tarefa):
    global tarefas
    tarefas = [ t for t in tarefas if t[0].lower() != tarefa.lower()]
    
def buscar_tarefa(tarefa):
    resultado = [ t for t in tarefas if t[0].lower() == tarefa.lower()]
    print()
    if resultado:
        for tarefa, status in resultado:
            print(f'Tarefa encontrada: {tarefa} - {status}')
            print()
        return
    print(f'Tarefa não encontrada: {tarefa}')
    print()
    
 
while True:
    os.system('cls | clear')
    print()
    print('Bem vindo ao Gerenciador de Tarefas')
    print('-' * 50)
    print()
    print('Adionar Tarefa - 1')
    print('Listar Tarefas - 2')
    print('Remover Tarefa - 3')
    print('Buscar Tarefa - 4')
    print('Concluir Tarefa - 5')
    print('Sair - 0')
    print()
    comand = int(input('Digite o número do comando que deseja: '))
    print()
    match comand:
        case 1:
            adicionar_tarefas(input('Qual tarefa deseja adicionar: '))
        case 2:
            listar_tarefas()
        case 3:
            remover_tarefa(input('Qual tarefa deseja remover: '))
        case 4:
            buscar_tarefa(input('Qual tarefa deseja buscar: '))
        case 5:
            concluir_tarefa(input('Qual tarefa deseja concluir: '))
        case 0:
            print('Finalizando gerenciador de tarefas...')
            break
        case _:
            print(f'Comando {comand} desconhecido, por favor digite entre os comando conhecidos ')
    print()
    input('Presione enter para continuar')

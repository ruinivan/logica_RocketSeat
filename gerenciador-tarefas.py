tarefas = []

def adicionar_tarefas(tarefa):
    tarefas.append((tarefa, 'pendente'))

def listar_tarefas():
    global tarefas
    for t in tarefas:
        print(f'{t[0]} - {t[1]}')
        
def concluir_tarefa(tarefa):
    global tarefas
    tarefas = [(t[0], 'concluída') if t[0] == tarefa else t for t in tarefas]

def remover_tarefa(tarefa):
    global tarefas
    tarefas = [ t for t in tarefas if t[0] != tarefa]
    
def buscar_tarefa(tarefa):
    resultado = [ t for t in tarefas if t[0] == tarefa]
    if resultado:
        for tarefa, status in resultado:
            print(f'Tarefa encontrada: {tarefa} - {status}')
        return
    print(f'Tarefa não encontrada: {tarefa}')
    
 
adicionar_tarefas('Arrumar a Cama')
adicionar_tarefas('Lavar a louça')
adicionar_tarefas('Colocar o lixo para fora')
listar_tarefas()
print('Concluido tarefa de colocar o lixo para fora')
concluir_tarefa('Colocar o lixo para fora')
listar_tarefas()
print('Removendo tarefa de Arrumar a Cama')
remover_tarefa('Arrumar a Cama')
listar_tarefas()
print('Encontrando Lavar Louça')
buscar_tarefa('Lavar a louça')
buscar_tarefa('Lavar o carro')


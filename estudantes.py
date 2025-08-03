estudantes = {
    1: {'nome': 'Ana', 'idade': 45, 'curso': 'Computação'},
    2: {'nome': 'Ivan', 'idade': 70, 'curso': 'Matemática'},
    3: {'nome': 'Jaqueline', 'idade': 12, 'curso': 'Computação'}
}

cursos = ['Computação', 'Matemática', 'Física']

estudantes_cursos = {
    'Computação': {1, 3},
    'Matemática': {2}
}

def adicionar_estudante(matricula, nome, idade, curso):
    pessoa= {'nome': nome, 'idade': idade, 'curso': curso}
    estudantes[matricula] = pessoa
    if not curso in estudantes_cursos:
        estudantes_cursos[curso] = set()
    estudantes_cursos[curso].add(matricula)
    
print(estudantes_cursos)
adicionar_estudante(5, 'Victor', 19, 'Engenharia')
print(estudantes_cursos)
    
tarefas = []

def add_tarefa(descricao, prazo_final=None, urgencia='Média'):
    tarefa = {
        'ID': len(tarefas) + 1,
        'descricao': descricao,
        'status': 'Pendente',
        'prazo_final': prazo_final,
        'urgencia': urgencia
    }
    tarefas.append(tarefa)
    print(f"Tarefa '{descricao}' adicionada com sucesso!'")

def mostrar_tarefas():
    if tarefas:
        for tarefa in tarefas:
            print(f"ID: {tarefa['ID']} | Descrição: {tarefa['descricao']} | Status: {tarefa['status']} | "
                  f'Prazo Final: {tarefa['prazo_final']} | Urgência: {tarefa['urgencia']}')
    else:
        print('Não há tarefas pendentes.')


def check(id_tarefa):
    for tarefa in tarefas:
        if tarefa['ID'] == id_tarefa:
            tarefa['status'] = 'Concluída'
            print(f'Tarefa ID {id_tarefa} marcada como concluída')
            return
    print(f'Tarefa com ID {id_tarefa} não encontrada')


def deletar_tarefa(id_tarefa):
    for tarefa in tarefas:
        if tarefa['ID'] == id_tarefa:
            tarefas.remove(tarefa)
            print(f'Tarefa ID {id_tarefa} deletada com sucesso')
            return
    print(f'Tarefa com ID {id_tarefa} não encontrada')


def exibir_menu():
    while True:
        print('\n=== Gerenciador de Tarefas ===')
        print('1 - Adicionar Tarefa')
        print('2 - Listar Tarefas')
        print('3 - Marcar Concluída')
        print('4 - Deletar Tarefa')
        print('5 - Sair')

        escolha = input('Escolha uma opção: ')

        if escolha == '1':
            descricao = input('Insira a descrição da tarefa: ')
            prazo_final = input('Insira o prazo final (opcional): ')
            urgencia = input('Insira a urgência (Alta, Média, Baixa): ')
            add_tarefa(descricao, prazo_final, urgencia)
        elif escolha == '2':
            mostrar_tarefas()
        elif escolha == '3':
            id_tarefa = int(input('Insira o ID da tarefa a ser marcada como concluída: '))
            check(id_tarefa)
        elif escolha == '4':
            id_tarefa = int(input('Insira o ID da tarefa a ser deletada: '))
            deletar_tarefa(id_tarefa)
        elif escolha == '5':
            print('Saindo...')
            break
        else:
            print('Erro: opção inválida.')


exibir_menu()

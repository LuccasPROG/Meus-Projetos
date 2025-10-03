tarefas_diaria = []
def guardar_tarefas(tarefa, horario):
    dados = {'tarefas': tarefa, 'horario': horario}
    tarefas_diaria.append(dados)

def mostrar_tarefas():
    print('-='*15)
    print('       TAREFAS DIARIAS')
    print('-='*15)

    for dados in tarefas_diaria:
        print(f"{dados['tarefas']} Horario: {dados['horario']:.2f}")



while True:
    tarefas = str(input('Digite uma tarefa (ou "sair" para encerrar) :')).upper().strip()
    if tarefas == 'SAIR':
        break
    horario = (input('Digite um horario:'))
    entrada = horario.replace(':','.')
    horario = float(entrada)
    guardar_tarefas(tarefas, horario)
mostrar_tarefas()
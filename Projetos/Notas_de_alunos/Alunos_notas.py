alunos = []
def cadastrar_alunos(nomes, notas):
    aluno = {'nome': nomes, 'nota': notas}
    alunos.append(aluno)

def mostrar_alunos():
    print('-='*15)
    print('      DADOS DOS ALUNOS')
    print('-='*15)
    for aluno in alunos:
        print(f"- {aluno['nome']} Nota: {aluno['nota']}")

#INICIO
while True:
    nome = str(input('Digite o nome do aluno (ou "sair" para encerrar): ')).upper()
    if nome == 'SAIR':
        break   
    nota = float(input(f'Digite a nota de {nome} :'))
    cadastrar_alunos(nome, nota)

mostrar_alunos()
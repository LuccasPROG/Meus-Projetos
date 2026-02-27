#SISTEMA
import os
import json

def adicionar_coisas_a_lista(comando, caminho_arquivo):
    lista_de_tarefas.append(comando)
    criar_json_e_salvar(lista_de_tarefas, caminho_arquivo)
    print(f'Comando: {comando} Adicionado a lista de tarefas')

def listar(lista):
    if not lista:
        print('Não existe nada na lista ainda!')
        return 
    
    print('Tarefas:')
    for i, item in enumerate(lista, start=1):
        print(f'{i}) {item}')
    print()


def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe!')
        criar_json_e_salvar(tarefas, caminho_arquivo)
    return dados


def criar_json_e_salvar(tarefas, caminho_arquivo):
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
      json.dump(tarefas, arquivo, indent=2)


CAMINHO_ARQUIVO = 'tarefas.json'
lista_de_tarefas = ler([], CAMINHO_ARQUIVO)
lista_de_desfazer = []


while True:
    print('Comandos: listar, desfazer, refazer, sair')
    comando = input('Digite uma tarefa ou comando: ')

    if comando == 'listar':
        os.system('cls')
        listar(lista_de_tarefas)

    elif comando == 'desfazer':
        os.system('cls')
        if lista_de_tarefas:
            desfeito = lista_de_tarefas.pop()
            lista_de_desfazer.append(desfeito)
            criar_json_e_salvar(lista_de_tarefas, CAMINHO_ARQUIVO)
            print(f'O Item {desfeito} foi retirado com sucesso!')
        else:
            print('Não a Nada para desfazer!')

    elif comando == 'refazer':
        os.system('cls')
        if lista_de_desfazer:
            refazer = lista_de_desfazer.pop()
            lista_de_tarefas.append(refazer)
            criar_json_e_salvar(lista_de_tarefas, CAMINHO_ARQUIVO)
            print(f'O item {refazer} foi colocado na lista novamente!')
        else:
            print('Não a Nada Para Refazer!')

    elif comando == 'sair':
        break
    else:

        adicionar_coisas_a_lista(comando, CAMINHO_ARQUIVO)
        continue
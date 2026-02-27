import time
import json
import os
estoque = []
def linha():
    ''' Faz linhas mais rapido'''
    print('-='*20)

def cadastro_de_produtos(nome, preco, quantidade, codigo):
    '''
    Essa função ela vai cadastra os nomes e precos do estoque e jogar na lista estoque
    '''
    codigo_existe = False # validação se o codigo ta duplicado
    produto = {
             'nome': nome,
             'preco': preco,
             'quantidade' : quantidade,
             'codigo' : codigo,
        }
    for produto_existente in estoque:# Essa repetição serve para ve se o codigo existe caso sim codigo existe recebe true
        if produto_existente['codigo'] == codigo: 
            codigo_existe = True
            break

    if codigo_existe: # esse if informa se o codigo ja exister o error!
        print('\033[1;31mERROR❌: Esse codigo já existe\033[m')
        time.sleep(1)
        print('\033[1;31mERROR❌: Não foi possivel fazer o cadastro!\033[m')
        time.sleep(1)
        input('Aperte ENTER para continuar ...')


    else:# e essa caso não exista o codigo igual ela cria e adiciona na lista!
        time.sleep(1)
        print('\033[1;32mCadastro feito com Sucesso!✅\033[m')
        time.sleep(1)
        estoque.append(produto)
        input('Aperte ENTER para continuar ...')

        with open('estoque.json', 'w') as arquivo:
            json.dump(estoque, arquivo, indent=4)

        os.system('cls')



while True:
    try: # validando caso veja algum erro de numero ou letra digitada errada
        linha()
        print('           Sistema de Estoque')
        linha()

        print('''1. Cadastrar Produtos
2. Calcular o Total de Produtos em Estoque
3. Mostrar Produtos estoque
4. Sair''')

        opcao = int(input('Digite sua Opção:'))
    except  ValueError:
        print('\033[1;31mError❌: Você digitou um numero invalido!\033[m')
        continue
    except:
        print('\033[1;31mError❌: Erro não cadastrado!\033[m')
        continue


    if opcao == 1:
        try:
            nome = str(input('Digite o Nome do produto: '))

            preco = float(input('Digite o Preço do produto: '))
            
            
            while preco < 0: #validação caso o preço seja menor que 0
                print('\033[1;31mError❌: Você digitou um preço negativo!\033[m')
                time.sleep(1)
                preco = float(input('Digite o Preço do produto: '))

            quantidade = int(input('Digite a quantidade de produtos: '))
            while quantidade < 0:
                print('\033[1;31mError❌: Você digitou uma quantidade negativa!\033[m')
                time.sleep(1)
                quantidade = int(input('Digite a quantidade de produtos: '))

            codigo = int(input('Digite o codigo do produto: '))


            cadastro_de_produtos(nome, preco, quantidade, codigo)
        except  ValueError:
            print('\033[1;31mError❌: Você digitou um numero invalido!\033[m')
            continue
        except:
            print('\033[1;31mError❌: Erro não cadastrado!\033[m')


    elif opcao == 2:
        total = 0
        for produto in estoque:
            total += produto['quantidade']
        print(f'Total de Produto no estoque: {total}')
        time.sleep(2)
        input('Aperte ENTER para continuar ...')
        os.system('cls')



    elif opcao == 3:
        linha()
        print('                 Estoque')
        linha()

        with open('estoque.json', 'r') as arquivo:# carrega o arquivo json
            lista_de_estoque = json.load(arquivo)


        for indice, produto in enumerate(lista_de_estoque):
            print(f"{indice + 1}) Nome: {produto['nome']}, Preço: {produto['preco']:.2f}, Quantidade: {produto['quantidade']}, Codigo: {produto['codigo']}.")
            time.sleep(1)
        input('Aperte ENTER para continuar ...')
        os.system('cls')


    elif opcao == 4:
        os.system('cls')
        print('Encerrando',end='')
        time.sleep(1)
        print('.',end='')
        time.sleep(1)
        print('.')
        
        print('Volte sempre!👌')
        break


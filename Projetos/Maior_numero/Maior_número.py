maior = menor = None

while True:
    try:
        numero = int(input('Digite um número: '))
    except ValueError:
        print('\033[1;31mERRO: Digite um número inteiro valido! \033[m')
        continue

    if maior is None and menor is None:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero

        if numero < menor:
            menor = numero

    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar? [S/N] : ').strip().upper()[0]
        if resp not in 'SN':
            print('\033[1;31mERRO: Digite um S ou N \033[m')
    if resp == 'N':
        break
print('-='*15)
print(f'O maior número digitado é {maior}')
print(f'O menor número digitado é {menor}')
print()
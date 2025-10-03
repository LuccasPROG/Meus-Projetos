try:
    while True:
        c = float(input('Digite uma temperatura em C° :'))
        fah = (c * 9/5) + 32
        print(f'a temperatura {c}c° em Fahrenheit é \033[33m{fah}\033[m')
        resp = ' '
        while resp not in 'NS':
            resp = str(input('Deseja Continuar?[S/N]:')).strip().upper()[0]
            if resp not in 'NS':
                print('\033[31mErro: Digite S ou N\033[m')
                continue
        if resp == 'N':
            break
    print('\033[1;34m>> Obrigado por usar o conversor, volte sempre! <<\033[m')
except (ValueError):
    print('ERRO: Digite um numero inteiro valido!')
    
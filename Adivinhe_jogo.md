secret_number = 777

print(
"""
+===================================+
| Bem vindo ao meu jogo, trouxa!    |
| Insira um número inteiro          |
| e adivinhar o número que tenho    |
| escolhidos para você.             |
| Então, qual é o número secreto?   |
+===================================+
""")
numero = int(input('Numero:'))
while secret_number != numero:
    print('Ha ha! Você está preso no meu loop!')
    numero = int(input('Numero:'))
print('Muito bem, trouxa! Você está livre agora.')

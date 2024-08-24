from random import randint
from time import sleep
itens=('Pedra', 'Papel','Tesoura')
computador = randint(0,2)
print('''Suas opções
[0]Pedra 
[1] Papel
[2] Tesoura  ''')
JOGADOR =int(input('Qual o jogador deseja jogar'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('computador jogou {}'.format(itens[computador]))
print('jogador jogou {} '.format(itens[JOGADOR]))
if computador == 0:
    if JOGADOR == 0:
        print('EMPATE')
    elif JOGADOR == 1:
         print('JOGADOR VENCEU')
    elif JOGADOR == 2:
        print('Computador VENCEU')
    else:
        print('JOGADA INVALIDA ')
if computador == 1:
    if JOGADOR == 0:
        print('COMPUTADOR VENCEU')
    elif JOGADOR == 1:
            print('EMPATE')
    elif JOGADOR == 2:
     print('JOGADOR VENCEU')
    else:
      print('JOGADA INVALIDA')
if computador == 2:
    if JOGADOR == 0:
        print('JOGADOR VENCEU')
    elif JOGADOR == 1:
        print('COMPUTADOR VENCEU')
    elif JOGADOR == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')












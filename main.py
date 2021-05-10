import random
from termcolor import colored


def cria_baralho():  # Primeira função na página do EP2
    cartas = []
    embaralhado = []
    naipe = ['♠', '♥', '♦', '♣']  # red, cyan, magenta, green
    k = -1
    while len(cartas) != 52:  # Repete o loop a seguir 4 vezes, mudando o naipe
        k += 1
        for i in range(2, 15):  # Coloca as cartas de 2 a A
            if i == 11:
                i = 'J'
            elif i == 12:
                i = 'Q'
            elif i == 13:
                i = 'K'
            elif i == 14:
                i = 'A'
            cartas.append(str(i) + naipe[k])  # Junta o número da carta com o naipe
    while len(cartas) > 0:  # Embaralha a sequência de cartas
        embaralhado.append(cartas[random.randint(0, len(cartas) - 1)])
        cartas.remove(embaralhado[len(embaralhado) - 1])
    return embaralhado  # Cartas são dadas assim


def extrai_naipe(carta):  # Segunda função na página do EP2
    naipe = carta[-1]  # Selecionar a última posição = naipe
    return naipe


def extrai_valor(carta):  # Terceira função na página do EP2
    if len(carta) == 2:  # Se for um número de um algarismo, pegar somente a primeira posição
        return carta[0]
    if len(carta) == 3:  # Se for um número de dois algarismos, pegar as duas primeiras posições
        return carta[0:2]


def lista_movimentos_possiveis(b, i):  # Quarta função na página do EP2  -> b = baralho; i = índice
    mov_pos = []  # Lista de movimentos possíveis
    if i == 0:
        return mov_pos
    if i < len(b) and i > 0 and extrai_naipe(b[i]) == extrai_naipe(b[i - 1]) or extrai_valor(b[i]) == extrai_valor(
            b[i - 1]):
        mov_pos.append(1)
    if (i - 3) < 0:
        return mov_pos
    if i < len(b) and i > 2 and extrai_naipe(b[i]) == extrai_naipe(b[i - 3]) or extrai_valor(b[i]) == extrai_valor(
            b[i - 3]):
        mov_pos.append(3)
    return mov_pos


def empilha(baralho, i, f):  # Quinta função na página do EP2
    if (i - f) == 1:  # Se for trocar com a anterior, simplesmente apagar a anterior (o destino)
        del baralho[f]
        return baralho
    if (i - f) == 3:  # Se for trocar com 3 cartas anteriores, destino = origem. Apagar origem
        baralho[f] = baralho[i]
        del baralho[i]
        return baralho


def possui_movimentos_possiveis(baralho):  # Sexta e última função da página do EP2
    for i in range(0, len(baralho)):  # Olhando para uma carta de cada vez, ver se ela tem algum movimento possível
        movimentos = lista_movimentos_possiveis(baralho, i)
        if len(movimentos) > 0:  # Se alguma das cartas puder ser movida, retornar True
            return True
    return False  # Se não tiver, retornar False


def print_colorido(carta):  # Devolve uma cor para a carta dependendo do naipe
    cor = ''
    if extrai_naipe(carta) == '♠':
        cor = 'red'
    elif extrai_naipe(carta) == '♥':
        cor = 'cyan'
    elif extrai_naipe(carta) == '♦':
        cor = 'magenta'
    elif extrai_naipe(carta) == '♣':
        cor = 'green'
    return cor


def imprime_b_atual(baralho):  # Essa função imprime o baralho atual linha por linha indicando o numero das cartas
    for carta in baralho:
        print('{}.'.format(baralho_atual.index(carta) + 1), colored('{}'.format(carta), print_colorido(carta)))
    return None


def eh_int(j):  # Impede que trave o programa se o usuário não digitar um int
    e_int = False
    while not e_int:
        if j.isnumeric():
            j = float(j)
        if j in range(1, len(baralho_atual) + 1):
            return True, int(j)
        j = input('Esse não é um número válido. Digite um número entre 1 e {}'.format(len(baralho_atual)))


print('''
PACIÊNCIA ACORDEÃO
~~~~~~~~~~~~~~~~~~
Bem-vindo(a) ao PACIÊNCIA ACORDEÃO!
O objetivo do jogo é empilhar todas as cartas sobre uma única pilha.
Há duas maneiras de empilhar:
1. Empilhar uma carta escolhida sobre a carta imediatamente anterior a ela
2. Empilhar a carta escolhida sobre a carta tres casas atrás da escolhida
Para que o movimento seja realizado, uma das duas condições a seguir precisa ser cumprida:
1. As duas cartas devem ter o mesmo naipe OU
2. As duas cartas devem ter o mesmo número
''')

jogar = True
while jogar:
    vamo = input('''Então, vamos jogar?!
    Digite "sim" para iniciar): ''')
    if vamo.lower() != 'sim':
        print('''Esperamos que tenha se divertido!''')
        break

    baralho_atual = cria_baralho()

    while possui_movimentos_possiveis(baralho_atual):  # Continua possibilitando jogadas até não haver mais

        imprime_b_atual(baralho_atual)  # Imprime o baralho
        jogada = input('Escolha uma carta para empilhar: ')  # Jogador escolhe uma carta
        jogada = eh_int(jogada)[1]  # Verifica se é um número válido

        possivel = lista_movimentos_possiveis(baralho_atual, jogada - 1)
        while len(possivel) == 0:
            print('\nA carta', baralho_atual[jogada - 1], 'Não pode ser empilhada')
            jogada = input('Escolha outra carta para empilhar: ')
            jogada = eh_int(jogada)[1]
            possivel = lista_movimentos_possiveis(baralho_atual, (jogada - 1))

        if len(possivel) == 1 and possivel[0] == 1:  # Se só é empilhável com a anterior
            empilha(baralho_atual, jogada - 1, jogada - 2)
        elif len(possivel) == 1 and possivel[0] == 3:  # Se só é empilhável com a 3a anterior
            empilha(baralho_atual, jogada - 1, jogada - 4)
        elif len(possivel) == 2:  # Se há dois movimentos possíveis
            print('{}. {}'.format((jogada - 3),
                              colored(baralho_atual[jogada - 4], print_colorido(baralho_atual[jogada - 4]))))
            print('{}. {}'.format((jogada - 1),
                              colored(baralho_atual[jogada - 2], print_colorido(baralho_atual[jogada - 2]))))
            jogada_f = input('Escolha uma carta para empilhar: ')
            jogada_f = eh_int(jogada_f)[1]
            while jogada_f != baralho_atual.index(baralho_atual[jogada - 1]) and jogada_f != baralho_atual.index(
                    baralho_atual[jogada - 3]):
                jogada_f = input('Essa carta não pode ser empilhada, digite o número de outra carta: ')
                jogada_f = eh_int(jogada_f)[1]
            empilha(baralho_atual, jogada - 1, jogada_f - 1)

    imprime_b_atual(baralho_atual)
    if len(baralho_atual) == 1:
        print('GANHOU!')
    else:
        print('PERDEU!')

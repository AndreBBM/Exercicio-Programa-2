import random


def cria_baralho():  # Primeira função na página do EP2
    cartas = []
    embaralhado = []
    naipe = ['♠', '♥', '♦', '♣']
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


def imprime_b_atual(baralho):  # Essa função imprime o baralho atual linha por linha indicando o numero das cartas
    for carta in baralho:
        print(str(baralho.index(carta) + 1) + '.', carta)
    return None


def eh_int(J, resposta_negativa):
    e_int = False
    while e_int == False:
        if J.isnumeric():
            J = float(J)
        else:
            e_int = False
        if J in range(1, len(baralho_atual) + 1):
            return True, int(J)
        else:
            e_int = False
        J = input(resposta_negativa)



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

vamo = input('''Então, vamos jogar?!
(digite "sim" para iniciar)''')
while vamo.lower() != 'sim':
    vamo = input('''Então, vamos jogar?!''')

baralho_atual = cria_baralho()

while possui_movimentos_possiveis(baralho_atual):   #Continua possibilitando jogadas até não haver mais

    imprime_b_atual(baralho_atual)
    jogada = input('Escolha uma carta para empilhar')
    jogada = eh_int(jogada, 'Digite algo válido')[1]

    possivel = lista_movimentos_possiveis(baralho_atual, jogada - 1)
    while len(possivel) == 0:
        print('\nA carta', baralho_atual[jogada - 1], 'Não pode ser empilhada')
        jogada = input('Escolha outra carta para empilhar')
        jogada = eh_int(jogada, 'Digite algo válido')[1]
        possivel = lista_movimentos_possiveis(baralho_atual, (jogada - 1))

    if len(possivel) == 1 and possivel[0] == 1:  # Se só é impilhável com a anterior
        empilha(baralho_atual, jogada - 1, jogada - 2)
    elif len(possivel) == 1 and possivel[0] == 3:  # se só é impilhável com a 3a anterior
        empilha(baralho_atual, jogada - 1, jogada - 4)
    elif len(possivel) == 2:  # Se há dois movimentos possíveis
        print(str(baralho_atual.index(baralho_atual[jogada - 1]) - 2) + '.', baralho_atual[jogada - 4] + '\n' +
              str(baralho_atual.index(baralho_atual[jogada - 1])) + '.', baralho_atual[jogada - 2])
        jogada_f = input('escolha uma carta para empilhar')
        jogada_f = eh_int(jogada_f, 'Digite algo válido')[1]
        while jogada_f != baralho_atual.index(baralho_atual[jogada - 1]) and jogada_f != baralho_atual.index(
                baralho_atual[jogada - 3]):
            jogada_f = input('Essa carta não pode ser empilhada, digite o número de outra carta')
            jogada_f = eh_int(jogada_f, 'Digite algo válido')[1]
        empilha(baralho_atual, jogada - 1, jogada_f - 1)

imprime_b_atual(baralho_atual)
if len(baralho_atual) == 1:
    print('GANHOU!')
else:
    print('PERDEU!')

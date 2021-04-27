import random

def cria_baralho():             # Primeira função na página do EP2
    cartas = []
    embaralhado = []
    naipe = ['♠', '♥', '♦', '♣']
    k = -1
    while len(cartas) != 52:    # Repete o loop a seguir 4 vezes, mudando o naipe
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
            cartas.append(str(i) + naipe[k])
    while len(cartas) > 0:      # Embaralha a sequência de cartas
        embaralhado.append(cartas[random.randint(0, len(cartas) - 1)])
        cartas.remove(embaralhado[len(embaralhado) - 1])
    return embaralhado          # Cartas são dadas assim

def extrai_naipe(carta):        # Segunda função na página do EP2
    naipe = carta[-1]
    return naipe
# Escolher qual das duas usar
def extrai_naipe(carta):
     if len(carta) == 3:
         naipe = carta[2]
     else:
         naipe = carta[1]
     return naipe

def extrai_valor(carta):        # Terceira função na página do EP2
    if len(carta) == 2:
        return carta[0]
    if len(carta) == 3:
        return carta[0:2]

def lista_movimentos_possiveis(b,i):  # Quarta função na página do EP2  -> b = baralho; i = índice
    mov_pos = []                      # Lista de movimentos possíveis
    if i == 0:                      
        return mov_pos
    if i < len(b) and i > 0 and extrai_naipe(b[i]) == extrai_naipe(b[i-1]) or extrai_valor(b[i]) == extrai_valor(b[i-1]):
        mov_pos.append(1)
    if i == 2 and extrai_naipe(b[i]) != extrai_naipe(b[i-1]) and extrai_valor(b[i]) != extrai_valor(b[i-1]):
        return mov_pos
    if (i - 3) < 0:
        return mov_pos
    if i < len(b) and i > 2 and extrai_naipe(b[i]) == extrai_naipe(b[i-3]) or extrai_valor(b[i]) == extrai_valor(b[i-3]):
        mov_pos.append(3)
    return mov_pos

    # INCOMPLETA #
def empilha(baralho, i, f):     # Quinta função na página do EP2
    destino = baralho[f]
    origem = baralho[i]
    del baralho[f]
    return baralho
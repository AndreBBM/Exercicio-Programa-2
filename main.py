import random


def cria_baralho():             #Primeira função na página do EP2
    cartas = []
    embaralhado = []
    naipe = ['♠', '♥', '♦', '♣']
    k = -1
    while len(cartas) != 52:    #repete o loop a seguir 4 vezes, mudando o naipe
        k += 1
        for i in range(2, 15):  #dá as cartas de 2 a A
            if i == 11:
                i = 'J'
            elif i == 12:
                i = 'Q'
            elif i == 13:
                i = 'K'
            elif i == 14:
                i = 'A'
            cartas.append(str(i) + naipe[k])
    while len(cartas) > 0:      #Embaralha a sequência de cartas
        embaralhado.append(cartas[random.randint(0, len(cartas) - 1)])
        cartas.remove(embaralhado[len(embaralhado) - 1])
    return embaralhado
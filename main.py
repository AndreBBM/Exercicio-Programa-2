def extrai_naipe(carta):
    if len(carta) == 3:
        naipe = carta[2]
    else:
        naipe = carta[1]
    return naipe


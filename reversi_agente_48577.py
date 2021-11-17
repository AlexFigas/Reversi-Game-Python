from random import choice

from reversi_motor_48577 import get_jogadas_possiveis


def jogada_agente(jogo):
    jogadas = get_jogadas_possiveis(jogo)
    return choice(jogadas)

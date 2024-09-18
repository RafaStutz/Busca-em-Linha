from typing import Callable, List, Tuple

from utils.calcula_ponto import calcula_ponto

from busca.passo_constante import passo_constante


def golden_section(
    funcao: Callable[[float, float], float],
    tolerancia: float = 1e-5,
    direcao: Tuple[float, float] = (1, 1),
    ponto_inicial: Tuple[float, float] = (0, 0),
) -> Tuple[float, float, int, List[Tuple[float, float]], List[float]]:
    alfa_U, alfa_L, pontos, valores, iter_passo_constante = passo_constante(
        funcao, armazenar_pontos=True, direcao=direcao, ponto_inicial=ponto_inicial
    )

    x1_atual, x2_atual = calcula_ponto(alfa_L, ponto_inicial, direcao)
    valor_atual = funcao(x1_atual, x2_atual)

    # Teste direção inicial
    eps = 1e-6
    alfa_eps = alfa_L + eps
    x1_eps, x2_eps = calcula_ponto(alfa_eps, ponto_inicial, direcao)
    valor_eps = funcao(x1_eps, x2_eps)

    if valor_eps > valor_atual:
        direcao = (-direcao[0], -direcao[1])

    RA = (5**0.5 - 1) / 2

    beta = alfa_U - alfa_L

    alfa_E = alfa_L + (1 - RA) * beta
    alfa_D = alfa_L + RA * beta

    x1_E, x2_E = calcula_ponto(alfa_E, ponto_inicial, direcao)
    f1 = funcao(x1_E, x2_E)

    x1_D, x2_D = calcula_ponto(alfa_D, ponto_inicial, direcao)
    f2 = funcao(x1_D, x2_D)

    iteracoes = 0

    valores.append(f1)
    valores.append(f2)

    while abs(alfa_U - alfa_L) > tolerancia:
        beta = alfa_U - alfa_L

        if f1 > f2:
            alfa_L = alfa_E

            alfa_E = alfa_D
            f1 = f2

            alfa_D = alfa_L + RA * beta
            x1_D, x2_D = calcula_ponto(alfa_D, ponto_inicial, direcao)
            f2 = funcao(x1_D, x2_D)
            valores.append(f2)
        else:
            alfa_U = alfa_D

            alfa_D = alfa_E
            f2 = f1

            alfa_E = alfa_L + (1 - RA) * beta
            x1_E, x2_E = calcula_ponto(alfa_E, ponto_inicial, direcao)
            f1 = funcao(x1_E, x2_E)
            valores.append(f1)

        iteracoes += 1

    alfa_final = (alfa_U + alfa_L) / 2
    x1_final, x2_final = calcula_ponto(alfa_final, ponto_inicial, direcao)

    iteracoes_totais = iter_passo_constante + iteracoes

    return x1_final, x2_final, iteracoes_totais, pontos, valores

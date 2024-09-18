from typing import Callable, Tuple

from utils.calcula_ponto import calcula_ponto

from busca.passo_constante import passo_constante


def bissecao(
    funcao: Callable[[float, float], float],
    erro: float = 1e-8,
    tolerancia: float = 1e-5,
    direcao: Tuple[float, float] = (1, 1),
    ponto_inicial: Tuple[float, float] = (0, 0),
) -> tuple[float, float, int, list[tuple[float, float]], list[float]]:
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

    iteracoes_bissecao = 0
    while abs(alfa_U - alfa_L) > tolerancia:
        ponto_medio = (alfa_L + alfa_U) / 2
        print(
            f"Iter {iteracoes_bissecao}: alfa_L={alfa_L}, alfa_U={alfa_U}, ponto_medio={ponto_medio}"
        )

        x1_medio1, x2_medio1 = calcula_ponto(ponto_medio - erro, ponto_inicial, direcao)
        x1_medio2, x2_medio2 = calcula_ponto(ponto_medio + erro, ponto_inicial, direcao)

        f1 = funcao(x1_medio1, x2_medio1)
        f2 = funcao(x1_medio2, x2_medio2)

        if f1 > f2:
            alfa_L = ponto_medio
            valores.append(f2)
        else:
            alfa_U = ponto_medio
            valores.append(f1)

        iteracoes_bissecao += 1

    ponto_medio_final = (alfa_U + alfa_L) / 2
    x1_final, x2_final = calcula_ponto(ponto_medio_final, ponto_inicial, direcao)

    iteracoes_totais = iter_passo_constante + iteracoes_bissecao

    return x1_final, x2_final, iteracoes_totais, pontos, valores

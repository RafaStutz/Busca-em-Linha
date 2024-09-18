from typing import Callable, List, Tuple

from utils import calcula_ponto


def passo_constante(
    funcao: Callable[[float, float], float],
    passo: float = 0.01,
    alfa_L: float = 0.0,
    max_iter: int = 10000000,
    direcao: Tuple[float, float] = (1, 1),
    ponto_inicial: Tuple[float, float] = (0, 0),
    armazenar_pontos: bool = False,
) -> Tuple[float, float, List[Tuple[float, float]], List[float], int]:
    pontos = []
    valores = []

    x1_atual, x2_atual = calcula_ponto(alfa_L, ponto_inicial, direcao)
    valor_atual = funcao(x1_atual, x2_atual)

    # Teste de direção
    eps = 1e-6
    alfa_eps = alfa_L + eps
    x1_eps, x2_eps = calcula_ponto(alfa_eps, ponto_inicial, direcao)
    valor_eps = funcao(x1_eps, x2_eps)

    if valor_eps > valor_atual:
        direcao = (-direcao[0], -direcao[1])

    if armazenar_pontos:
        pontos.append((x1_atual, x2_atual))

    alfa_U = alfa_L + passo
    x1_proximo, x2_proximo = calcula_ponto(alfa_U, ponto_inicial, direcao)
    valor_proximo = funcao(x1_proximo, x2_proximo)
    iter_count = 0

    while valor_proximo < valor_atual and iter_count < max_iter:
        alfa_L = alfa_U
        valor_atual = valor_proximo

        if armazenar_pontos:
            pontos.append((x1_proximo, x2_proximo))

        alfa_U = alfa_L + passo
        x1_proximo, x2_proximo = calcula_ponto(alfa_U, ponto_inicial, direcao)
        valor_proximo = funcao(x1_proximo, x2_proximo)

        iter_count += 1
        valores.append((valor_proximo))

    if armazenar_pontos:
        return alfa_U, alfa_L, pontos, valores, iter_count
    else:
        return alfa_U, alfa_L, [], [], iter_count

def calcula_ponto(
    alfa: float, ponto_inicial: tuple[float, float], direcao: tuple[float, float]
) -> tuple[float, float]:
    x1 = ponto_inicial[0] + alfa * direcao[0]
    x2 = ponto_inicial[1] + alfa * direcao[1]

    return x1, x2

from typing import Callable, Tuple

import matplotlib.pyplot as plt
import numpy as np


def plotar_curvas_de_nivel(
    funcao: Callable[[float, float], float],
    ponto_inicial: Tuple[float, float],
    ponto_final: Tuple[float, float],
    pontos_intermediarios: list[tuple[float, float]],
    metodo: str,
    nome_funcao: str,
    salvar_imagem: bool = False,
    formato: str = "svg",
) -> None:
    x1_vals = np.linspace(-8, 8, 400)
    x2_vals = np.linspace(-8, 8, 400)
    X1, X2 = np.meshgrid(x1_vals, x2_vals)

    Z = np.array(
        [[funcao(x1, x2) for x1, x2 in zip(row_x1, row_x2)] for row_x1, row_x2 in zip(X1, X2)]
    )

    plt.contour(X1, X2, Z, levels=50, cmap="inferno", linewidth=0.5)
    contorno = plt.contour(X1, X2, Z, levels=20, cmap="inferno", linewidth=0.5)
    plt.clabel(contorno, inline=True, fontsize=9, fmt="%1.1f")

    if metodo == "passo_constante":
        line_style = "--"
        marker_style = "o"
        color = "blue"
        label = "Passos Intermediários (Passo Constante)"
    elif metodo == "bissecao":
        line_style = "-."
        marker_style = "x"
        color = "orange"
        label = "Passos Intermediários (Bisseção)"
    elif metodo == "golden_section":
        line_style = "-"
        marker_style = "o"
        color = "gray"
        label = "Passos Intermediários (Seção Áurea)"
    else:
        line_style = "-"
        marker_style = "o"
        color = "pink"
        label = "Passos Intermediários"

    pontos_x = [p[0] for p in pontos_intermediarios]
    pontos_y = [p[1] for p in pontos_intermediarios]
    plt.plot(
        pontos_x,
        pontos_y,
        marker=marker_style,
        label=label,
        markersize=1,
        linestyle=line_style,
        color=color,
    )

    plt.scatter(
        ponto_inicial[0], ponto_inicial[1], color="red", label="Ponto Inicial", s=120, marker="D"
    )
    plt.scatter(
        ponto_final[0], ponto_final[1], color="green", label="Ponto Final", s=120, marker="X"
    )

    plt.title(f"Busca em Linha com {metodo} - {nome_funcao}")
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.legend()
    plt.grid(True)

    if salvar_imagem:
        nome_arquivo = f"{nome_funcao}_{metodo}.{formato}"
        plt.savefig(nome_arquivo, format=formato, dpi=300)
        print(f"Imagem salva como: {nome_arquivo}")

    plt.show()

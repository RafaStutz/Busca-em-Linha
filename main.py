from dataclasses import dataclass
from typing import Callable, List, Tuple

from benchmark import Himmelblau, McCormick, funcao_quadratica
from busca.bissecao import bissecao
from busca.golden_section import golden_section
from busca.passo_constante import passo_constante
from utils.plotar_curvas_de_nivel import plotar_curvas_de_nivel


@dataclass
class ResultadoOtimizacao:
    ponto_final: Tuple[float, float]
    pontos: List[Tuple[float, float]]
    valores: List[float]
    iteracoes: int = 0


@dataclass
class Funcao:
    nome: str
    funcao: Callable[[float, float], float]
    ponto_inicial: Tuple[float, float]
    direcao: Tuple[float, float]


def rodar_otimizacao_e_plotar(
    funcao: Callable[[float, float], float],
    ponto_inicial: Tuple[float, float],
    direcao: Tuple[float, float],
    nome_funcao: str,
    metodo: str = "passo_constante",
    salvar_imagem: bool = True,
    formato: str = "svg",
) -> None:
    def executar_passo_constante() -> ResultadoOtimizacao:
        alfa_U, alfa_L, pontos, valores, iteracoes = passo_constante(
            funcao, armazenar_pontos=True, direcao=direcao, ponto_inicial=ponto_inicial
        )
        ponto_final = pontos[-1]
        return ResultadoOtimizacao(ponto_final, pontos, valores, iteracoes)

    def executar_bissecao() -> ResultadoOtimizacao:
        x1_final, x2_final, iteracoes, pontos, valores = bissecao(
            funcao, direcao=direcao, ponto_inicial=ponto_inicial
        )
        ponto_final = (x1_final, x2_final)
        return ResultadoOtimizacao(ponto_final, pontos, valores, iteracoes)

    def executar_golden_section() -> ResultadoOtimizacao:
        x1_final, x2_final, iteracoes, pontos, valores = golden_section(
            funcao, direcao=direcao, ponto_inicial=ponto_inicial
        )
        ponto_final = (x1_final, x2_final)
        return ResultadoOtimizacao(ponto_final, pontos, valores, iteracoes)

    metodos_disponiveis = {
        "passo_constante": executar_passo_constante,
        "bissecao": executar_bissecao,
        "golden_section": executar_golden_section,
    }

    if metodo not in metodos_disponiveis:
        raise ValueError(
            f"Método '{metodo}' não é válido. Escolha entre 'passo_constante', 'bissecao' ou 'golden_section'."
        )

    resultado: ResultadoOtimizacao = metodos_disponiveis[metodo]()

    print(f"Função {nome_funcao} - {metodo.capitalize()}")
    print(f"Ponto inicial: {ponto_inicial}")
    print(f"Ponto final encontrado: {resultado.ponto_final}")
    print(f"Direção: {direcao}")
    print(f"Valores da função: {resultado.valores}")
    if metodo:
        print(f"Número de iterações: {resultado.iteracoes}")
    print()

    plotar_curvas_de_nivel(
        funcao, ponto_inicial, resultado.ponto_final, resultado.pontos, metodo, nome_funcao
    )


def main() -> None:
    funcoes = [
        Funcao(
            nome="Função Quadrática",
            funcao=funcao_quadratica,
            ponto_inicial=(1, 2),
            direcao=(-1, -2),
        ),
        Funcao(
            nome="Função McCormick",
            funcao=McCormick,
            ponto_inicial=(-2, 3),
            direcao=(1.453, -4.547),
        ),
        Funcao(
            nome="Função Himmelblau",
            funcao=Himmelblau,
            ponto_inicial=(0, 5),
            direcao=(3, 1.5),
        ),
    ]

    metodos = ["passo_constante", "bissecao", "golden_section"]

    for funcao_data in funcoes:
        for metodo in metodos:
            print(f"Rodando otimização para {funcao_data.nome} usando o método {metodo}")
            rodar_otimizacao_e_plotar(
                funcao_data.funcao,
                funcao_data.ponto_inicial,
                funcao_data.direcao,
                funcao_data.nome,
                metodo,
                salvar_imagem=True,
                formato="svg",
            )


if __name__ == "__main__":
    main()

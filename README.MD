# Otimização de Funções com Busca em Linha

Este projeto implementa três métodos de busca linear (line search) para funções de benchmark, incluindo `passo_constante`, `bissecao`, e `golden_section`. O código executa esses métodos nas funções de benchmark e gera gráficos das curvas de nível mostrando a evolução da otimização.

## Requisitos

Certifique-se de ter Python instalado. Para rodar o projeto, é necessário instalar as bibliotecas abaixo:

```bash
pip install matplotlib numpy

```
# Como Rodar o Projeto

1. Clonar o Repositório:

Clone este repositório para o seu ambiente local:

```bash
git clone https://github.com/RafaStutz/Busca-em-Linha.git
```
2. Executar o Script:

Para rodar o projeto, execute o arquivo principal main.py. Ele realizará busca em linha nas funções de benchmark (Função Quadrática, Função McCormick, e Função Himmelblau) utilizando os três métodos disponíveis (passo_constante, bissecao, e golden_section). Os métodos necessitam de um ponto inicial e uma direção. 

```bash
python main.py
```
3. Saída Esperada:

O script irá imprimir no console os resultados da otimização para cada função e método, incluindo:

- Ponto inicial
- Ponto final encontrado
- Direção da otimização
- Valores da função ao longo das iterações
- Número de iterações

## Estrutura

```
.
├── busca/
│   ├── bissecao.py
│   ├── golden_section.py
│   └── passo_constante.py
├── utils/
│   └── plotar_curvas_de_nivel.py
├── benchmark.py
└── main.py
```

- busca/: Contém implementações dos métodos de busca.
- utils/: Contém utilitários, como a função de plotagem de curvas de nível.
- benchmark.py: Define as funções de benchmark que serão otimizadas.
- main.py: Script principal que coordena a otimização e a geração dos gráficos.
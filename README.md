# Pac-Man — Algoritmo Minimax

## Disciplina

Inteligência Artificial — Ciências da Computação

## Trabalho

Implementação do Algoritmo Minimax para Pac-Man

## Professor

Nikson Bernardes Fernandes Ferreira

## Objetivo

O Pac-Man escolhe cada jogada com o algoritmo Minimax, olhando alguns turnos
à frente na árvore do jogo:

- **Pac-Man é o MAX** — entre suas ações legais, escolhe a que leva ao estado
  de maior valor;
- **os fantasmas são os MIN** — a busca assume que cada um joga da forma mais
  desfavorável possível para o Pac-Man.

O valor de cada folha da árvore vem de `self.evaluationFunction`.

## Arquivo principal da atividade

`seuPacManAgents.py` — classe `MinimaxAgent`, método `getAction`.

## Requisitos

- Python 3 (testado em 3.11)
- Nenhuma biblioteca externa. O projeto usa apenas a biblioteca padrão.

Para a janela gráfica é preciso ter `tkinter` instalado (vem junto com a
maioria das instalações do Python). Sem ele, use os modos texto (`-t`) ou
silencioso (`-q`), descritos abaixo.

## Como executar

A partir da pasta do projeto:

```bash
python pacman.py --pacman MinimaxAgent
```

Profundidade 1:

```bash
python pacman.py --pacman MinimaxAgent -a depth=1
```

Profundidade 2:

```bash
python pacman.py --pacman MinimaxAgent -a depth=2
```

Em um mapa pequeno, que deixa os testes mais rápidos:

```bash
python pacman.py --pacman MinimaxAgent -a depth=2 -l minimaxClassic
```

Sem interface gráfica (modo texto ou silencioso):

```bash
python pacman.py --pacman MinimaxAgent -a depth=2 -l minimaxClassic -t
python pacman.py --pacman MinimaxAgent -a depth=2 -l minimaxClassic -q
```

> **Sobre a profundidade:** o guia do projeto mostra `--depth 2`, mas o
> `pacman.py` desta versão não tem essa opção de linha de comando — ele
> responde `error: no such option: --depth`. A profundidade é passada como
> argumento do agente, por `-a depth=N` (equivalente a `--agentArgs depth=N`).
> Sem esse argumento, vale o padrão da classe `MultiAgentSearchAgent`, que é 3.
> A profundidade precisa ser no mínimo 1.

## Estrutura

| Arquivo / pasta | Papel |
|---|---|
| `seuPacManAgents.py` | **arquivo desta atividade** — contém `MinimaxAgent` e a implementação do Minimax |
| `pacman.py` | motor do jogo, regras, `GameState` e a leitura da linha de comando |
| `game.py` | estruturas base: `Agent`, `Directions`, `AgentState`, laço de execução |
| `multiAgents.py` | `MultiAgentSearchAgent` (fornece `self.index`, `self.depth` e `self.evaluationFunction`), `ReflexAgent` e as funções de avaliação |
| `ghostAgents.py` | comportamento dos fantasmas (`RandomGhost`, `DirectionalGhost`) |
| `layouts/` | mapas do jogo em `.lay` (`minimaxClassic`, `smallClassic`, `mediumClassic`, ...) |
| `test_cases/` | casos de teste do projeto original, incluindo as árvores Minimax de `q2` |
| `docs/` | material da disciplina e a análise do projeto |

## Implementação

Toda a lógica fica na função `minimax` aninhada em `MinimaxAgent.getAction`.

- **Pac-Man = MAX** (`agentIndex == 0`), **fantasmas = MIN** (`agentIndex > 0`).
- A recursão para quando o jogo termina (`isWin()` / `isLose()`), quando a
  profundidade máxima é atingida (`depth == self.depth`) ou quando o agente da
  vez não tem nenhuma ação legal. Nos três casos o estado é avaliado por
  `self.evaluationFunction`.
- Os agentes se revezam na ordem `0, 1, 2, ...` até o último fantasma, e então
  o turno volta ao Pac-Man. **A profundidade aumenta apenas nessa volta**, ou
  seja, depois que todos os fantasmas completaram suas jogadas — uma unidade de
  profundidade é um ciclo completo.
- A quantidade de fantasmas vem de `state.getNumAgents()`, então a mesma
  implementação funciona com um ou vários fantasmas.
- Apenas a chamada da raiz devolve uma ação (`North`, `South`, `East`, `West`
  ou `Stop`); todas as chamadas internas devolvem valores numéricos.

## Testes executados

Validações rodadas nesta versão do código:

- `python3 -m py_compile seuPacManAgents.py pacman.py game.py multiAgents.py ghostAgents.py` — sem erros;
- os 33 casos `GraphGameTreeTest` de `test_cases/q2`, comparados com os
  arquivos `.solution` do projeto original (ação escolhida e conjunto de nós
  gerados): **33 de 33 corretos**, incluindo os testes que verificam o
  incremento da profundidade com um e com dois fantasmas;
- `python3 pacman.py --pacman MinimaxAgent -a depth=1 -l minimaxClassic -q -f` — vitória;
- `python3 pacman.py --pacman MinimaxAgent -a depth=2 -l minimaxClassic -q -f` — vitória;
- `python3 pacman.py --pacman MinimaxAgent -q -f` (padrão, `mediumClassic`) — vitória.

Vitória não é garantida em toda partida: o resultado depende do mapa, do número
de fantasmas e da função de avaliação usada. Em `minimaxClassic`, um mapa
apertado com 3 fantasmas, uma amostra de 5 partidas ficou em 2 vitórias tanto
com `depth=1` quanto com `depth=2`.

## Créditos

O projeto Pac-Man foi desenvolvido na UC Berkeley por John DeNero e Dan Klein,
com o autograder de Brad Miller, Nick Hay e Pieter Abbeel — http://ai.berkeley.edu.
Os cabeçalhos de licença e atribuição dos arquivos originais foram preservados.

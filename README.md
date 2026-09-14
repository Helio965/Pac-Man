# Pac-Man — Projeto Minimax (Inteligência Artificial)

Repositório de trabalho do projeto de implementação do algoritmo **Minimax**
para o agente Pac-Man.

Disciplina: Inteligência Artificial — Ciências da Computação
Professor: Nikson Bernardes Fernandes Ferreira

## Estrutura

```
docs/
  ANALISE.md                    análise consolidada dos materiais + do código
  guia-projeto-minimax.txt      texto do guia do projeto
  aula3-busca.txt               texto da Aula 3 (Busca de Soluções)
  aula5-busca-heuristica.md     transcrição da Aula 5 (Busca Heurística)
  agentes-inteligentes.md       transcrição de Agentes Inteligentes
  originais/                    os 4 PDFs originais

pacman/                         projeto Berkeley Pac-Man AI (do pacman.zip)
  seuPacManAgents.py            <- arquivo a implementar e entregar
```

## Onde o trabalho acontece

O objetivo é implementar a função `minimax` dentro de
`MinimaxAgent.getAction`, em **`pacman/seuPacManAgents.py`**. Esse é também o
único arquivo a ser entregue.

## Como rodar

Sempre a partir da pasta `pacman/`:

```bash
cd pacman

# Minimax com profundidade 2, layout pequeno, modo texto
python3 pacman.py -p MinimaxAgent -a depth=2 -l minimaxClassic -t

# sem gráficos, 10 partidas (avaliação de desempenho)
python3 pacman.py -p MinimaxAgent -a depth=2 -l minimaxClassic -q -n 10
```

> A flag `--depth` citada na seção 6 do guia **não existe** em `pacman.py`; a
> profundidade se passa por `-a depth=N`. Veja `docs/ANALISE.md` §4 para esse e
> outros pontos de atenção verificados.

## Estado atual

Materiais analisados e arquivados. `MinimaxAgent` ainda está com o esqueleto
original do professor — nenhuma implementação foi feita, aguardando as próximas
instruções.

## Créditos

O projeto Pac-Man foi desenvolvido na UC Berkeley (John DeNero e Dan Klein;
autograder por Brad Miller, Nick Hay e Pieter Abbeel) — http://ai.berkeley.edu.

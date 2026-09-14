# Análise dos Materiais — Projeto Minimax para Pac-Man

Disciplina: Inteligência Artificial — Análise e Desenvolvimento de Sistemas
Professor: Nikson Bernardes Fernandes Ferreira

Este documento consolida a análise dos PDFs da disciplina e do código-fonte entregues.
Os arquivos originais estão em `docs/originais/`, as transcrições em `docs/`,
e o projeto executável na raiz do repositório.

---

## 1. Inventário do que foi salvo

| Arquivo no repositório | Origem | Formato |
|---|---|---|
| `docs/originais/Guia-do-Projeto-Minimax-Pac-Man.pdf` | Guia do Projeto (9 seções) | PDF com texto |
| `docs/originais/IA-Aula3-Busca.pdf` | Aula 3 — Busca de Soluções | PDF com texto |
| `docs/originais/IA-Aula5-Busca-Heuristica.pdf` | Aula 5 — Busca Heurística | PDF só imagem (32 slides) |
| `docs/originais/IA-Agentes-Inteligentes.pdf` | Agentes Inteligentes | PDF só imagem (27 slides) |
| `docs/guia-projeto-minimax.txt` | texto extraído do guia | TXT |
| `docs/aula3-busca.txt` | texto extraído da Aula 3 | TXT |
| `docs/aula5-busca-heuristica.md` | transcrição manual (slides em imagem) | Markdown |
| `docs/agentes-inteligentes.md` | transcrição manual (slides em imagem) | Markdown |
| `docs/originais/IA-Aula4-Busca-Cega.pdf` | Aula 4 — Tipos de Busca (Busca Cega) | PDF só imagem (35 slides) |
| `docs/originais/IA-Aula9-Aprendizagem-de-Maquina.pdf` | Aula 9 — Aprendizagem de Máquina | PDF só imagem (64 slides) |
| `docs/originais/IA-Aula11-Aprendizado-Profundo-CNN.pdf` | Aula 11 — Aprendizado Profundo / CNN | PDF com texto (53 slides) |
| raiz do repositório | conteúdo de `pacman.zip` (`pacman.py`, `game.py`, `layouts/`, `test_cases/`, ...) | código |

Os PDFs de slides marcados como "só imagem" não possuem camada de texto — os
dois primeiros (Aula 5 e Agentes Inteligentes) foram lidos página a página e
transcritos em Markdown.

As Aulas 4, 9 e 11 chegaram depois e estão arquivadas como referência da
disciplina. Elas não entram na implementação: a Aula 4 cobre busca cega
(largura e profundidade, evitar estados repetidos — Russell & Norvig cap. 3),
e as Aulas 9 e 11 cobrem aprendizado de máquina e redes convolucionais. O
trabalho pedido é busca adversarial Minimax, um tema distinto.

---

## 2. O que cada documento pede/ensina

### 2.1 Guia do Projeto (documento normativo)

É o documento que define a entrega. Pontos operativos:

- **Onde codificar:** arquivo `seuPacManAgents.py`, método `getAction` da
  classe `MinimaxAgent`, na função aninhada `minimax(agentIndex, depth, state)`.
- **Entrega:** apenas o arquivo `seuPacManAgents.py`, no espaço aluno.
- **Regras de recursão exigidas:**
  - Caso base: `state.isWin()`, `state.isLose()` ou `depth == self.depth`
    → retornar `self.evaluationFunction(state)`.
  - Próximo agente: se `agentIndex == state.getNumAgents() - 1` → volta para
    `0` (Pac-Man); senão `agentIndex + 1`.
  - Profundidade: incrementa **apenas** quando o último fantasma terminou a
    jogada (ou seja, ao fechar uma rodada completa de todos os agentes).
  - `agentIndex == 0` → maximização (inicia em `-float('inf')`).
  - `agentIndex > 0` → minimização (inicia em `float('inf')`).
  - A **chamada mais externa retorna a ação**; as chamadas recursivas retornam
    **apenas o valor**. Essa assimetria é o detalhe que mais gera erro.
  - Tratar agente sem ações legais (encurralado).
- **Critérios de avaliação:** correção do algoritmo, desempenho do Pac-Man,
  compreensão conceitual e qualidade do código (organização e comentários).

### 2.2 Aula 3 — Busca de Soluções (Russell & Norvig, cap. 3)

Base conceitual: formulação de problema (estado inicial, conjunto de
ações/operadores, teste de término, custo de caminho), espaço de estados,
solução como *caminho* e não como estado final, solução ótima, custo total =
custo de busca + custo de caminho, abstração válida/útil, algoritmo genérico de
geração e teste com fronteira, componentes do nó (estado, pai, ação, `g(n)`,
profundidade), e os 4 critérios de avaliação de estratégias: **completude,
otimalidade, custo de tempo e custo de memória**. Distingue busca cega de busca
heurística.

### 2.3 Aula 5 — Busca Heurística

Busca informada: função de avaliação baseada em heurística `h`. Busca Gulosa
(usa só `h`; barata, mas nem completa nem ótima) versus **A\*** (`f(n) = g(n) +
h(n)`; completa, ótima e de eficiência ótima quando `h` é admissível — nunca
superestima — e consistente/monotônica). Exemplos: Canudos→Petrolândia e
Arad→Bucharest. Custo de memória `O(b^d)`.

**Conexão com o projeto:** a `evaluationFunction` do Minimax cumpre o mesmo
papel que a heurística `h` da Aula 5 — é a estimativa aplicada nas folhas
quando a busca é cortada por profundidade.

### 2.4 Agentes Inteligentes (Russell & Norvig, cap. 2)

Agente = entidade que percebe o ambiente por **sensores** e age por
**atuadores**; propriedades (autonomia, reatividade, pró-atividade,
sociabilidade); função do agente `f: P* → A`; medida de desempenho; agente
racional (maximiza a medida de desempenho esperada) versus onisciente;
`agente = arquitetura + programa`; e os cinco tipos básicos: reativo simples,
reativo baseado em modelo, baseado em objetivos, baseado em utilidade e com
aprendizagem.

**Conexão com o projeto:** o `MinimaxAgent` é um **agente baseado em
utilidade** — a `evaluationFunction` é a função de utilidade, e o Pac-Man
escolhe a ação que a maximiza sob a suposição de fantasmas adversariais.

---

## 3. Análise do código do projeto

### 3.1 Estado inicial, antes da implementação

`seuPacManAgents.py` vinha com o esqueleto terminando em `pass` — ou seja,
`minimax()` retornava `None` e o jogo quebrava com:

```
Exception: Illegal action None
```

(verificado com `python3 pacman.py -p MinimaxAgent -l minimaxClassic -q -f`).
Era o comportamento esperado de um esqueleto não implementado.

O restante do projeto já estava funcional: `python3 pacman.py -p GreedyAgent -l
smallClassic -q -f` rodava até o fim normalmente.

O Minimax foi implementado depois disso; veja a seção 6.

### 3.2 API do `GameState` relevante ao Minimax

| Método | Uso |
|---|---|
| `state.getLegalActions(agentIndex)` | ações do agente da vez |
| `state.generateSuccessor(agentIndex, action)` | próximo estado |
| `state.getNumAgents()` | 1 (Pac-Man) + nº de fantasmas |
| `state.isWin()` / `state.isLose()` | teste de término |
| `self.evaluationFunction(state)` | valor da folha |
| `self.depth` | profundidade máxima (`MultiAgentSearchAgent.__init__`, padrão `'3'`) |
| `self.index` | sempre `0` (Pac-Man) |

Atenção: `generateSuccessor` levanta `Exception('Can't generate a successor of
a terminal state.')` — por isso o teste de `isWin`/`isLose` precisa vir **antes**
de gerar sucessores.

### 3.3 Como o agente é descoberto

`pacman.py::loadAgent` varre os diretórios do `PYTHONPATH` (mais `.`) buscando
arquivos terminados em `gents.py`. `seuPacManAgents.py` casa com esse padrão,
então `-p MinimaxAgent` encontra a classe sem configuração extra — desde que o
comando seja executado **de dentro da pasta do projeto**.

---

## 4. Pontos de atenção encontrados

Cinco pontos relevantes entre o guia/código e o comportamento real, todos
verificados por execução:

### 4.1 A flag `--depth` do guia não existe

A seção 6 do guia manda rodar:

```bash
python3 pacman.py --pacman MinimaxAgent --depth 2
```

Isso falha, porque `pacman.py` não define essa opção:

```
pacman.py: error: no such option: --depth
```

A forma correta de passar profundidade é via `-a` / `--agentArgs`, que alimenta
o construtor de `MultiAgentSearchAgent`:

```bash
python3 pacman.py -p MinimaxAgent -a depth=2 -l minimaxClassic
```

### 4.2 `betterEvaluationFunction` está com os sinais invertidos

Em `seuPacManAgents.py` (e idêntica em `multiAgents.py`):

```python
return currentGameState.getScore() - (1.5 / (minFoodDistance + 1)) + (2 / (minGhostDistance + 1))
```

Os dois termos empurram o Pac-Man na direção errada:

- `- 1.5/(minFoodDistance + 1)`: quanto **mais perto** da comida, **menor** a
  pontuação — pune aproximar-se da comida.
- `+ 2/(minGhostDistance + 1)`: quanto **mais perto** do fantasma, **maior** a
  pontuação — premia aproximar-se do fantasma.

O esperado seria o oposto (`+` para comida, `−` para fantasma). É código
fornecido pelo professor, então **não foi alterado** — fica registrado para
decisão de vocês. Note que a função só entra em jogo se for pedida
explicitamente (`-a evalFn=better`); o padrão é `scoreEvaluationFunction`.

Efeito colateral menor da mesma função: `min(ghostDistances)` levanta
`ValueError` se um layout não tiver fantasmas (`-k 0`).

### 4.3 O `autograder.py` não avalia esta entrega

`projectParams.py` fixa `STUDENT_CODE_DEFAULT = 'multiAgents.py'`, e os testes
`test_cases/q2/` resolvem o agente com `getattr(multiAgents, 'MinimaxAgent')`.
Como `MinimaxAgent` mora em `seuPacManAgents.py` (e `multiAgents.py` não tem a
classe `StaffMultiAgentSearchAgent` usada pelo teste `8-pacman-game`), rodar
`autograder.py -q q2` falha independentemente da implementação.

Os casos de teste em si, porém, continuam válidos e foram aproveitados: as 33
árvores `GraphGameTreeTest` de `test_cases/q2` foram rodadas contra o
`MinimaxAgent` de `seuPacManAgents.py` por um script de verificação avulso
(mantido fora do repositório, já que não faz parte da entrega), comparando a
ação escolhida e o conjunto de nós gerados com os arquivos `.solution`
oficiais. Resultado na seção 6.1.

### 4.4 Custo computacional dos padrões

O padrão de `pacman.py` é o layout `mediumClassic` com `depth=3` (padrão de
`MultiAgentSearchAgent`). A opção `-k` limita os fantasmas a no máximo 4, mas
quem manda é o mapa: contando os `G` nos arquivos `.lay`, `mediumClassic` tem
**2 fantasmas** e `minimaxClassic` tem **3**.

Então o comando padrão são 3 agentes × 3 de profundidade = 9 níveis de
recursão por jogada. É pesado, mas roda: uma partida completa levou **1m47s**
aqui. Já `minimaxClassic` com `depth=3` são 4 agentes = 12 níveis.

Para depurar rápido, use `depth=1` ou `depth=2`, como o guia recomenda na
seção 7 — nesses casos a partida termina em menos de um segundo.

### 4.5 Ambiente sem `tkinter`

Este container não tem `tkinter`, então a janela gráfica não abre aqui. Use
`-q` (sem gráficos) ou `-t` (texto) para rodar. Na máquina de vocês, com
Python completo, o modo gráfico funciona normalmente.

---

## 5. Comandos úteis

Todos executados a partir da raiz do repositório:

```bash
# jogo padrão (teclado, precisa de tkinter)
python3 pacman.py

# Minimax, profundidade 2, layout pequeno — modo texto
python3 pacman.py -p MinimaxAgent -a depth=2 -l minimaxClassic -t

# sem gráficos (útil para medir desempenho em lote)
python3 pacman.py -p MinimaxAgent -a depth=2 -l minimaxClassic -q -n 10

# com a função de avaliação alternativa
python3 pacman.py -p MinimaxAgent -a depth=2,evalFn=better -l smallClassic -q

# limitando o número de fantasmas (reduz o fator de ramificação)
python3 pacman.py -p MinimaxAgent -a depth=2 -l smallClassic -k 1 -q

# semente fixa: mesma partida toda vez (bom para comparar versões)
python3 pacman.py -p MinimaxAgent -a depth=2 -l minimaxClassic -q -f
```

---

## 6. Estado do trabalho

O Minimax foi implementado em `seuPacManAgents.py`, dentro de
`MinimaxAgent.getAction`. Nada fora dessa classe foi alterado: engine,
layouts, `test_cases/`, `betterEvaluationFunction` e os cabeçalhos de licença
da UC Berkeley seguem como vieram no `pacman.zip`.

Resumo da implementação:

- parada em `isWin()`, `isLose()` ou `depth == self.depth`, avaliando a folha
  com `self.evaluationFunction(state)`;
- agente sem ações legais também é avaliado, para o ramo não ficar valendo
  `-inf`/`+inf`;
- próximo agente = `0` quando o atual é o último fantasma, senão
  `agentIndex + 1`; a profundidade só cresce nessa volta ao Pac-Man;
- número de fantasmas lido de `state.getNumAgents()`, sem valor fixo;
- MAX no Pac-Man, MIN nos fantasmas;
- apenas a chamada da raiz devolve a ação, as demais devolvem o valor;
- `self.depth < 1` levanta `ValueError` com mensagem clara, em vez de deixar o
  erro aparecer adiante como `Illegal action 0.0`.

### 6.1 Validação executada

| Teste | Resultado |
|---|---|
| `py_compile` em `seuPacManAgents.py`, `pacman.py`, `game.py`, `multiAgents.py`, `ghostAgents.py` | sem erros |
| 33 casos `GraphGameTreeTest` de `test_cases/q2` conferidos contra os `.solution` (ação e nós gerados) | 33/33 corretos |
| `--pacman MinimaxAgent -a depth=1 -l minimaxClassic -q -f` | vitória, score 516 |
| `--pacman MinimaxAgent -a depth=2 -l minimaxClassic -q -f` | vitória, score 516 |
| `--pacman MinimaxAgent -q -f` (padrão, `mediumClassic`, depth 3) | vitória, score −829, 1m47s |
| `--pacman MinimaxAgent -a depth=2 -l smallClassic -k 1 -q -f` | vitória, score 930 |
| `--pacman MinimaxAgent -a depth=2 -l minimaxClassic -q -f -n 5` | 2 vitórias em 5 |

A verificação mais forte é a das árvores de `q2`: além da ação escolhida, ela
compara o **conjunto de nós gerados** com o gabarito oficial, o que confirma a
ordem de visita e o momento exato em que a profundidade é incrementada. Os
casos `7-1*` e `7-2*` existem justamente para checar isso com um e com dois
fantasmas.

Sobre o desempenho em partida: `minimaxClassic` é um mapa apertado com 3
fantasmas, e perder lá é comum — o Minimax assume fantasmas ótimos e, quando
a morte parece inevitável, não há jogada que a evite. Isso não indica erro no
algoritmo; a corretude é o que as árvores de `q2` atestam.

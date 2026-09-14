# Aula 5 — Busca Heurística

> Capítulo 3 — Russell & Norvig
>
> Transcrição dos slides de `docs/originais/IA-Aula5-Busca-Heuristica.pdf`.
> O PDF original é composto por imagens (sem camada de texto), por isso esta
> transcrição foi feita a partir da leitura página a página.

---

## Estratégias de Busca Exaustiva (Cega)

- Encontram soluções para problemas pela geração *sistemática* de novos estados,
  que são comparados ao objetivo.
- São *ineficientes* na maioria dos casos:
  - utilizam apenas o custo de caminho do nó atual ao nó inicial (**função g**)
    para decidir qual o próximo nó da fronteira a ser expandido;
  - essa medida nem sempre conduz a busca na direção do objetivo.
- Como encontrar um barco perdido?
  - não podemos procurar no oceano inteiro...
  - observamos as correntes marítimas, o vento, etc...

## Estratégias de Busca Heurística (Informada)

- Utilizam **conhecimento específico do problema** na escolha do próximo nó a
  ser expandido (barco perdido: correntes marítimas, vento, etc).
- Aplicação de uma **função de avaliação** a cada nó na fronteira do espaço de
  estados.
  - Essa função **estima o custo de caminho** do nó atual até o objetivo mais
    próximo utilizando uma **função heurística**.

## Classes de algoritmos para busca heurística

1. Busca pela melhor escolha (*Best-First search*)
2. Busca com limite de memória
3. Busca com melhora iterativa

---

## Busca pela Melhor Escolha (Best-First Search)

- **BME**: busca genérica onde o nó de menor custo "aparente" na fronteira do
  espaço de estados é expandido primeiro.
- Duas abordagens básicas:
  1. Busca Gulosa (*Greedy search*)
  2. Algoritmo A\*

### Algoritmo geral

- **Função-Insere**: insere novos nós na fronteira *ordenados* com base na
  Função-Avaliação, que por sua vez está baseada na função heurística.

```
função Busca-Melhor-Escolha (problema, Função-Avaliação)
        Busca-Genérica (problema, Função-Insere)
        retorna uma solução
```

---

## BME: Busca Gulosa

- Semelhante à busca em profundidade com *backtracking*.
- Tenta expandir o **nó mais próximo do nó final** com base na estimativa feita
  pela função heurística `h`.
- Função-Avaliação: a própria função heurística `h`.

### Funções Heurísticas

- Função heurística `h`: **estima** o custo do caminho mais barato do estado
  atual até o estado final mais próximo.
- Funções heurísticas são **específicas para cada problema**.
- Exemplo: encontrar a rota mais barata de Canudos a Petrolândia, com
  `h_dd(n)` = distância direta entre o nó `n` e o nó final.

### Como escolher uma boa função heurística?

- Ela deve ser **admissível**: nunca *superestimar* o custo real da solução.
- A distância direta (`h_dd`) é admissível porque o caminho mais curto entre
  dois pontos é sempre uma linha reta.

### Avaliação da Busca Gulosa

- **Custo de busca mínimo**: não expande nós fora do caminho.
- Porém **não é ótima** — escolhe o caminho mais econômico à primeira vista:
  - Belém do S. Francisco → Petrolândia = 4,4 unidades;
  - porém existe caminho mais curto de Canudos a Petrolândia:
    Jeremoabo → P. Afonso → Petrolândia = 4 unidades.
  - A rota via Belém do S. Francisco foi escolhida porque
    `h_dd(BSF) = 1,5 u.`, enquanto `h_dd(Jeremoabo) = 2,1 u.`
- **Não é completa**:
  - pode entrar em *looping* se não detectar a expansão de estados repetidos;
  - pode tentar desenvolver um caminho infinito.
- Custo de tempo e memória: `O(b^d)` — guarda todos os nós expandidos.

---

## BME: Algoritmo A\*

- A\* expande o nó de **menor valor de `f`** na fronteira do espaço de estados.
- Tenta minimizar o custo total da solução combinando:
  - **Busca Gulosa (h)** — econômica, porém não é completa nem ótima;
  - **Busca de Custo Uniforme (g)** — ineficiente, porém completa e ótima.
- Função de avaliação do A\*:

```
f(n) = g(n) + h(n)
  g(n) = distância de n ao nó inicial
  h(n) = distância estimada de n ao nó final
```

- Se `h` é admissível, então `f(n)` também é admissível — `f` nunca irá
  superestimar o custo real da melhor solução através de `n`, pois `g` guarda o
  valor exato do caminho já percorrido.
- No exemplo Canudos→Petrolândia, o A\* escolhe de fato a rota mais curta:
  - `f(BSF) = 2,5 u + 1,5 u = 4 u`
  - `f(Jeremoabo) = 1,5 u + 2,1 u = 3,6 u`

### Outro exemplo: viajar de Arad a Bucharest

Mapa da Romênia com distâncias em linha reta até Bucharest (Arad 366,
Bucharest 0, Craiova 160, Dobreta 242, Eforie 161, Fagaras 178, Giurgiu 77,
Hirsova 151, Iasi 226, Lugoj 244, Mehadia 241, Neamt 234, Oradea 380,
Pitesti 98, Rimnicu Vilcea 193, Sibiu 253, Timisoara 329, Urziceni 80,
Vaslui 199, Zerind 374).

Expansão passo a passo (`f = g + h`):

1. `Arad: 366 = 0 + 366`
2. `Sibiu: 393 = 140 + 253` | `Timisoara: 447 = 118 + 329` | `Zerind: 449 = 75 + 374`
3. Expande Sibiu → `Arad: 646 = 280 + 366` | `Fagaras: 415 = 239 + 176` |
   `Oradea: 671 = 291 + 380` | `Rimnicu Vilcea: 413 = 220 + 193`
4. Expande Rimnicu Vilcea → `Craiova: 526 = 366 + 160` | `Pitesti: 417 = 317 + 100` |
   `Sibiu: 553 = 300 + 253`
5. Expande Fagaras → `Sibiu: 591 = 338 + 253` | `Bucharest: 450 = 450 + 0`
6. Expande Pitesti → `Bucharest: 418 = 418 + 0` | `Craiova: 615 = 455 + 160` |
   `Rimnicu Vilcea: 607 = 414 + 193`

Pela **Busca Gulosa**, o caminho tomado seria via Fagaras (`h = 178`), chegando
a Bucharest com custo maior. **O A\* tomou um rumo diverso do algoritmo guloso:
o caminho ótimo.**

### Análise do comportamento do A\*

- A estratégia é **completa e ótima**.
- **Custo de tempo**: exponencial com o comprimento da solução, porém boas
  funções heurísticas diminuem significativamente esse custo — o fator de
  expansão fica próximo de 1.
- **Custo de memória**: `O(b^d)` — guarda todos os nós expandidos para
  possibilitar o *backtracking*.
- A estratégia apresenta **eficiência ótima**: nenhum outro algoritmo ótimo
  garante expandir menos nós.
- A\* só expande nós com `f(n) ≤ C*`, onde `C*` é o custo do caminho ótimo.
- Para garantir otimalidade do A\*, o valor de `f` em um caminho particular deve
  ser **não decrescente**: `f(sucessor(n)) ≥ f(n)` — o custo de cada nó gerado no
  mesmo caminho nunca é menor do que o custo de seus antecessores.

### Condição de monotonicidade

- `f = g + h` deve ser não decrescente:
  - `g` é não decrescente (para operadores não negativos) — custo real do
    caminho já percorrido;
  - `h` deve ser **não-crescente (consistente, monotônica)**: `h(n) ≥ h(sucessor(n))`
    — quanto mais próximo do nó final, menor o valor de `h`. Isso vale para a
    maioria das funções heurísticas.
- Quando `h` não é consistente, para garantir otimalidade do A\*:
  - quando `f(suc(n)) < f(n)`,
  - usa-se `f(suc(n)) = max( f(n), g(suc(n)) + h(suc(n)) )`.

### A\* define contornos

Com `f(n) ≤ C*`, o fator de expansão fica próximo de 1 — a busca se organiza em
contornos concêntricos de valor de `f` crescente ao redor do estado inicial
(contornos de 380, 400 e 420 no mapa da Romênia).

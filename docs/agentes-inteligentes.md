# Agentes Inteligentes

> Russell & Norvig, 2020 — Capítulo 2
>
> Transcrição dos slides de `docs/originais/IA-Agentes-Inteligentes.pdf`.
> O PDF original é composto por imagens (sem camada de texto), por isso esta
> transcrição foi feita a partir da leitura página a página.

---

## Conceito de Agente

### O que são Agentes?

> "Um agente é uma entidade que percebe seu ambiente através de **sensores** e
> age sobre esse ambiente através de **atuadores**" (Russell & Norvig)

**Propriedades:**

1. **Autonomia**: capacidade de operar sem intervenção humana constante
2. **Reatividade**: percepção do ambiente e resposta a mudanças
3. **Pró-atividade**: pode tomar iniciativas e perseguir objetivos
4. **Sociabilidade**: habilidade de interagir com outros agentes ou pessoas

### Agentes Inteligentes

- "Um Agente é um sistema que usa um modelo de IA para interagir com seu
  ambiente a fim de atingir um objetivo definido pelo usuário."
- "Combina raciocínio, planejamento e execução de ações (frequentemente por meio
  de ferramentas externas) para cumprir tarefas."
- São diferentes de meros programas, pois operam sob controle autônomo, percebem
  seu ambiente, adaptam-se às mudanças e são capazes de assumir metas.

### Exemplos

| Tipo | Sensores | Atuadores |
|---|---|---|
| **Agente humano** | olhos, ouvidos e outros órgãos | mãos, pernas, boca e outras partes do corpo |
| **Agente robótico** | câmeras e outros sensores | vários motores |
| **Agente de software** | entrada do teclado, conteúdo de arquivos, websites, banco de dados | tela, disco rígido, ação em ferramenta, *functions* |

---

## Acoplamento Agente e Ambiente

O agente recebe **percepções** (*percepts*) do ambiente pelos sensores — as
entradas perceptivas do agente em qualquer momento dado — e devolve **ações**
(*actions*) pelos atuadores. Entre os dois está a **função de agente**, que
mapeia qualquer sequência de percepções específica para uma ação.

### Mapeando Percepções em Ações

- O comportamento de um agente é dado abstratamente pela **função do agente**:

```
f = P* → A
```

- onde `P*` é uma sequência de percepções e `A` é uma ação.
- **Sequência de percepções**: histórico completo de tudo que o agente percebeu
  em seu ambiente.

---

## Exemplo: O Mundo do Aspirador de Pó

- **Percepções**: local e conteúdo. Exemplo: `[A, sujo]`
- **Ações**: Esquerda, Direita, Aspirar, NoOp

| Sequência de Percepções | Ação |
|---|---|
| `[A, Limpo]` | Direita |
| `[A, Sujo]` | Aspirar |
| `[B, Limpo]` | Esquerda |
| `[B, Sujo]` | Aspirar |
| `[A, Limpo], [A, Limpo]` | Direita |
| `[A, Limpo], [A, Sujo]` | Aspirar |
| ... | ... |
| `[A, Limpo], [A, Limpo], [A, Limpo]` | Direita |
| `[A, Limpo], [A, Limpo], [A, Sujo]` | Aspirar |

**Programa:** se o quadrado atual estiver sujo, então aspirar; caso contrário,
mover para o outro lado.

---

## Medindo o Desempenho de um Agente

- O agente deve tomar a ação "correta" baseado no que ele percebe para ter
  sucesso.
- O conceito de sucesso do agente depende de uma **medida de desempenho
  objetiva**. Exemplos: quantidade de sujeira aspirada, gasto de energia, gasto
  de tempo, quantidade de barulho gerado, etc.
- A medida de desempenho deve refletir o resultado realmente desejado no
  ambiente.

## Agente Racional

- Um agente que se comporta tão bem quanto possível.
- Sobre racionalidade, dependem quatro coisas:
  - a medida de desempenho que define o critério de sucesso;
  - o conhecimento anterior que o agente tem do ambiente;
  - as ações que o agente pode executar;
  - a sequência de percepções do agente até o momento.
- *Para cada sequência de percepções possível, um agente racional deve
  selecionar uma ação que se espera venha **maximizar sua medida de
  desempenho**, dada a evidência fornecida pela sequência de percepções e por
  qualquer conhecimento interno do agente.*

### Racionalidade vs. Onisciência

- Um agente onisciente sabe o resultado real de suas ações e pode agir de acordo
  com ele.
- **Estamos falando de agentes racionais e não oniscientes.**

### Aprendizado

Relacionado à função do agente:

- na projeção do agente;
- deliberação de sua próxima ação;
- coleta de informação e aprendizagem a partir de sua experiência (modificação
  de seu comportamento padrão).

### Autonomia

- Sem autonomia, o agente se baseia no conhecimento anterior de seu projetista e
  não em suas próprias percepções.
- Um agente racional deve ser autônomo: aprender o que puder para compensar um
  conhecimento prévio parcial ou incorreto.
- É necessário que os agentes tenham habilidades/mecanismos para aprender por si
  mesmos para terem autonomia.

---

## Programa de Agentes

```
Agente = arquitetura + programa
```

O programa de agente implementa a função de agente que mapeia percepções em
ações.

## Tipos Básicos de Agentes

1. **Agentes reativos simples** — regras condição-ação (*if-then*) aplicadas
   diretamente sobre "what the world is like now".
2. **Agentes reativos baseados em modelos** — mantêm um *state* interno, mais o
   conhecimento de "how the world evolves" e "what my actions do".
3. **Agentes baseados em objetivos** — acrescentam *goals* e a projeção "what it
   will be like if I do action A".
4. **Agentes baseados na utilidade** — acrescentam uma função de *utility*:
   "how happy I will be in such a state".
5. **Agentes com aprendizagem** — *performance element*, *critic* (com um
   *performance standard*), *learning element* e *problem generator*.

---

## Uso de Agentes

### Por que Utilizar Agentes?

**Melhor gerenciamento de tarefas complexas:**

- automação de processos que envolvem múltiplas fontes de informação;
- coordenação de ações e tomada de decisão baseada em diversos fatores.

**Escalabilidade:**

- agentes podem ser distribuídos para lidar com grandes volumes de dados ou
  tarefas.

**Adaptação e aprendizado:**

- possibilidade de incorporar técnicas de *Machine Learning* para melhoria
  contínua.

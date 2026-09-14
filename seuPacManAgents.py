# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent
from pacman import GameState
from multiAgents import MultiAgentSearchAgent


class MinimaxAgent(MultiAgentSearchAgent):
    """
    Agente que escolhe suas ações pelo algoritmo Minimax.

    O Pac-Man (agentIndex 0) é o jogador MAX: busca o maior valor possível.
    Cada fantasma (agentIndex > 0) é um jogador MIN: a busca assume que eles
    jogam da forma mais desfavorável possível para o Pac-Man.

    Uma unidade de profundidade corresponde a um ciclo completo de jogadas:
    o Pac-Man e todos os fantasmas jogando uma vez cada.
    """

    def getAction(self, gameState: GameState):
        """Seu código vem aqui
        Adicione o código para minimax
        """

        # A busca precisa de pelo menos um ciclo completo de jogadas para ter
        # ações a comparar. Com self.depth <= 0 não existe árvore alguma: a
        # raiz cairia direto na condição de parada e devolveria um número, o
        # que estouraria adiante como "Illegal action <número>". Avisa aqui,
        # onde a causa real fica visível.
        if self.depth < 1:
            raise ValueError(
                'MinimaxAgent precisa de profundidade >= 1 (recebido: %d). '
                'Use por exemplo: -a depth=2' % self.depth
            )

        def minimax(agentIndex=0, depth=0, state=gameState):
            """
            Percorre a árvore Minimax e devolve o valor numérico de `state`.

            Exceção: na chamada da raiz — o Pac-Man decidindo agora, isto é
            agentIndex == self.index e depth == 0 — devolve a *ação* escolhida,
            que é o que getAction precisa entregar ao jogo. A raiz é única:
            a profundidade só cresce quando o último fantasma joga, então
            nenhum outro nó do Pac-Man volta a ter depth == 0.
            """

            # Condição de parada: fim de jogo (vitória ou derrota) ou limite
            # de profundidade atingido. O estado vira uma folha da árvore e é
            # avaliado pela função de avaliação do agente.
            if state.isWin() or state.isLose() or depth == self.depth:
                return self.evaluationFunction(state)

            acoes = state.getLegalActions(agentIndex)

            # Caso extremo: o agente da vez não tem nenhuma ação legal
            # (encurralado). Avalia o estado em vez de deixar o ramo valendo
            # -inf/+inf, o que contaminaria a comparação nos níveis acima.
            if not acoes:
                # Na raiz é preciso devolver uma ação, e não um número.
                if agentIndex == self.index and depth == 0:
                    return Directions.STOP
                return self.evaluationFunction(state)

            # Próximo agente e próxima profundidade. Os agentes jogam em ordem
            # (0, 1, 2, ... até o último fantasma) e o turno então volta ao
            # Pac-Man. A profundidade só aumenta nessa volta, quando o ciclo
            # completo de jogadas terminou.
            ehUltimoFantasma = (agentIndex == state.getNumAgents() - 1)
            proximoAgente = 0 if ehUltimoFantasma else agentIndex + 1
            proximaProfundidade = depth + 1 if ehUltimoFantasma else depth

            if agentIndex == self.index:
                # ----- MAX: turno do Pac-Man -----
                melhorValor = -float('inf')
                melhorAcao = acoes[0]

                for acao in acoes:
                    # gera o estado resultante da ação e desce na árvore
                    sucessor = state.generateSuccessor(agentIndex, acao)
                    valor = minimax(proximoAgente, proximaProfundidade, sucessor)

                    # guarda o maior valor visto e a ação que levou até ele
                    if valor > melhorValor:
                        melhorValor = valor
                        melhorAcao = acao

                # A raiz entrega a melhor ação; os demais nós MAX, o valor.
                if depth == 0:
                    return melhorAcao
                return melhorValor

            # ----- MIN: turno de um fantasma -----
            piorValor = float('inf')

            for acao in acoes:
                # gera o estado resultante da ação e desce na árvore
                sucessor = state.generateSuccessor(agentIndex, acao)
                valor = minimax(proximoAgente, proximaProfundidade, sucessor)

                # o fantasma apenas propaga o menor valor para cima;
                # a ação dele não precisa ser devolvida
                if valor < piorValor:
                    piorValor = valor

            return piorValor

        return minimax()


def betterEvaluationFunction(currentGameState: GameState):
    pos = currentGameState.getPacmanPosition()
    food = currentGameState.getFood().asList()
    ghostStates = currentGameState.getGhostStates()

    # Calcula a distância de Manhattan para a comida mais próxima
    foodDistances = [manhattanDistance(pos, f) for f in food]
    if len(foodDistances) > 0:
        minFoodDistance = min(foodDistances)
    else:
        minFoodDistance = 0

    # Distância para o fantasma mais próximo
    ghostDistances = [manhattanDistance(pos, ghost.getPosition()) for ghost in ghostStates]
    minGhostDistance = min(ghostDistances)

    # Aumenta a pontuação se o fantasma estiver assustado, mas penaliza se estiver muito perto
    scaredTimes = [ghostState.scaredTimer for ghostState in ghostStates]
    if min(scaredTimes) > 0:
        minGhostDistance = 0  # Ignora fantasmas assustados

    return currentGameState.getScore() - (1.5 / (minFoodDistance + 1)) + (2 / (minGhostDistance + 1))

# Abbreviation
better = betterEvaluationFunction

# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getproximoNodos(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (proximoNodo,
        accion, stepCost), where 'proximoNodo' is a proximoNodo to the current
        state, 'accion' is the accion required to get there, and 'stepCost' is
        the incremental cost of expanding to that proximoNodo.
        """
        util.raiseNotDefined()

    def getCostOfacciones(self, acciones):
        """
         acciones: A list of acciones to take

        This method returns the total cost of a particular sequence of acciones.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    pilaNodos = util.Stack()
    visitados = set()
    estadoInicial = problem.getStartState()
    pilaNodos.push((estadoInicial, []))
    visitados.add(estadoInicial) 

    while not pilaNodos.isEmpty():
        estadoActual, acciones = pilaNodos.pop()

        if problem.isGoalState(estadoActual):
            return acciones

        for proximoNodo, accion, costo in problem.getSuccessors(estadoActual):
            if proximoNodo not in visitados:
                visitados.add(proximoNodo) 
                nuevaAccion = acciones + [accion]
                pilaNodos.push((proximoNodo, nuevaAccion))

    return []


def breadthFirstSearch(problem):
    colaNodos = util.Queue()
    visitados = set()
    estadoInicial = problem.getStartState()
    colaNodos.push((estadoInicial, []))
    visitados.add(estadoInicial) 

    while not colaNodos.isEmpty():
        estadoActual, acciones = colaNodos.pop()

        if problem.isGoalState(estadoActual):
            return acciones

        for proximoNodo, accion, costo in problem.getSuccessors(estadoActual):
            if proximoNodo not in visitados:
                visitados.add(proximoNodo) 
                nuevaAccion = acciones + [accion]
                colaNodos.push((proximoNodo, nuevaAccion))

    return []




def uniformCostSearch(problem):
    colaPrioridad = util.PriorityQueue()
    visitados = set()
    estadoInicial = problem.getStartState()
    colaPrioridad.push((estadoInicial, [], 0), 0)
    

    while not colaPrioridad.isEmpty():
        estadoActual, acciones, costoActual = colaPrioridad.pop()
        if problem.isGoalState(estadoActual):
            return acciones

        if estadoActual not in visitados:
            visitados.add(estadoActual)
            for proximoNodo, accion, costo in problem.getSuccessors(estadoActual):
                if proximoNodo not in visitados:
                    nuevoCosto = costoActual + costo 
                    nuevaAccion = acciones + [accion]
                    colaPrioridad.push((proximoNodo, nuevaAccion, nuevoCosto), nuevoCosto)
                    
    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    colaPrioridad = util.PriorityQueue()
    visitados = {}
    estado_inicial = problem.getStartState()
    colaPrioridad.push((estado_inicial, []), heuristic(estado_inicial, problem))
    visitados[estado_inicial] = 0

    while not colaPrioridad.isEmpty():
        estadoActual, acciones = colaPrioridad.pop()

        if problem.isGoalState(estadoActual):
            return acciones

        for sucesor, accion, costo in problem.getSuccessors(estadoActual):
            nuevo_costo = visitados[estadoActual] + costo
            if sucesor not in visitados or nuevo_costo < visitados[sucesor]:
                visitados[sucesor] = nuevo_costo
                prioridad = nuevo_costo + heuristic(sucesor, problem)
                colaPrioridad.push((sucesor, acciones + [accion]), prioridad)
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

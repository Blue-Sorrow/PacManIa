# eightpuzzle.py
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


import search
import random

# Module Classes

class BaseState:
    """
         Clase Minima
    """

    def __init__( self, par ):
        """
        
           Inicio, se dan parámetros (par) que 

        """
        self.estado = [par]
        estado = self.estado[:] # Haz una copia para no causar efectos secundarios

    def isGoal( self ):
        """

           Ve si estas en la meta

        """
        if self.estado == [7]: # Checa estado meta
            return True
        else:
            return False

    def legalMoves( self ):
        """
          Regresa la lista de estados siguientes

        """
        moves = []

        return moves

    def result(self, move):
        """

          Regresa el nuevo estado con el movimiento

        """
        estado = self.estado[:] # Haz una copia para no causar efectos secundarios
        """ Cuando no es valida
        else:
            raise "Illegal Move"
        """

        # Crea copia
        newPuzzle = self.estado

        # Haz move

        return newPuzzle

    # Utilidades
    def __eq__(self, other):
        """
            Sobrecarga '==' 
        """
        if self.estado != self.estado:
                return False
        else:
            return True

    def __hash__(self):
        return hash(str(self.estado))

    def __getAsciiString(self):
        """
          Regresa cadena
        """
        cadena = []

        return cadena

    def __str__(self):
        return self.__getAsciiString()

# TODO: Implementa métodos de la clase

class BareSearchProblem(search.SearchProblem):
    """
      Estado inicial
    """
    def __init__(self,puzzle):
        "Crea problema nuevo."
        self.puzzle = puzzle

    def getStartState(self):
        return puzzle

    def isGoalState(self,state):
        return state.isGoal()

    def getSuccessors(self,state):
        """
          Regresa lista de succesores
              deben ser tuplas (sucesor, accion, costo)
        """
        succ = []
        for a in state.legalMoves():
            succ.append((state.result(a), a, 1))
        return succ

    def getCostOfActions(self, actions):
        """
         Costo de accionex
        """
        return len(actions)

# Corre si te llaman
if __name__ == '__main__':
    puzzle = 7
    print(puzzle)

    problem = BareSearchProblem(puzzle)
    path = search.breadthFirstSearch(problem)
    print('BFS found a path of %d moves: %s' % (len(path), str(path)))
    curr = puzzle
    i = 1
    for a in path:
        curr = curr.result(a)
        print('Despues de %d move%s: %s' % (i, ("", "s")[i>1], a))
        print(curr)

        raw_input("Press return for the next state...")   # wait for key stroke
        i += 1

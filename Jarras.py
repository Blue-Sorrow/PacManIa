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

class Jarras:
    """
    El problema de las Jarras de acuerdo a Die Hard 3 
        Se deben llenar una jarra con 4 litros de agua.
        Para ello se tienen dos jarras de 3 y 5 litros inicialmente vacias.
        Solo se puede:
            - Llenar una jarra
            - Vaciar una jarra 
            - Vertir una jarra en la otra 

    """

    def __init__( self, j3=0, j5=0 ):
        """
          Dos jarras con capacidad de 3 y 5 litros
        """
        self.jarra3 = j3 
        self.jarra5 = j5

    def isGoal( self ):
        """
          Checa si la jarra de 5 tiene 4 litros
        """
        return self.jarra5 == 4
        
        return 

    def legalMoves( self ):
        """
          Los movimientos legales, siempre se pueden hacer todos 
        """
        moves = ['llena3','vacia3','vierte3a5','llena5','vacia5','vierte5a3']
        return moves

    def result(self, move):
        """
          Regresa un nuevo estado despues de haber hecho el movimiento

        NOTE: La funcion *no* cambia el objecto actual.  En vez de eso,
        regresa un nuevo objeto.
        """
        j3, j5 = self.jarra3, self.jarra5
        match move:
          case 'llena3':
             j3 = 3
          case 'vacia3':
             j3 = 0
          case 'llena5':
             j5 = 5
          case 'vacia5':
             j5 = 0
          case 'vierte3a5':
             transferencia = min(j3, 5 - j5)
             j3 -= transferencia
             j5 += transferencia
          case 'vierte5a3':
             transferencia = min(j5, 3 - j3)
             j5 -= transferencia
             j3 += transferencia
        return Jarras(j3, j5)

    # Utilities for comparison and display
    def __eq__(self, other):
        """
            Sobrecarga '==' para ver si dos estados son iguales.

        """
        return self.jarra3 == other.jarra3 and self.jarra5 == other.jarra5

    def __hash__(self):
        return hash(str(self.jarra3)+":"+str(self.jarra5))

    def __getAsciiString(self):
        """
          Representacion como Cadena
        """
        return f"Jarra de 3 litros: {self.jarra3}L, Jarra de 5 litros: {self.jarra5}L"


    def __str__(self):
        return self.__getAsciiString()

# Para hacer: Implementar los metodos en clase

class JarrasSearchProblem(search.SearchProblem):
    """
      Implementacion de SearchProblem para Jarras

      Cada estado es una instancia de la Jarra.
    """
    def __init__(self,jarras):
        "Crea un nuevo problema."
        self.jarras = jarras

    def getStartState(self):
        return self.jarras

    def isGoalState(self,state):
        return state.isGoal()

    def getSuccessors(self,state):
        """
          Regresa lista de tuplas (sucesor, accion, costoPaso) del  
          estado original y costo 1.0 para cada una
        """
        succ = []
        for movimiento in state.legalMoves():
            nuevoEstado = state.result(movimiento)
            succ.append((nuevoEstado,movimiento,1))
        return succ

    def getCostOfActions(self, actions):
        """
         acciones: una lista de acciones a realizar

        Este metodo regresa el costo total de una secuencia de acciones.
        """
        return len(actions)



if __name__ == '__main__':
    jarras = Jarras(0,0)
    print('El problema de las jarras:')
    print(jarras)

    problem = JarrasSearchProblem(jarras)
    path = search.breadthFirstSearch(problem)
    print('BFS encontro una solucion con %d acciones: %s' % (len(path), str(path)))
    curr = jarras
    i = 1
    for a in path:
        curr = curr.result(a)
        print('Despues de %d acciones%s: %s' % (i, ("", "s")[i>1], a))
        print(curr)

        input("Oprima <Entrar> para el siguiente estado...")   # wait for key stroke
        i += 1

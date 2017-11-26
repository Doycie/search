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

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
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
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    
    #Make a Stack for the open list for the states we want to check
    #In DFS we always want to check the deepest state, so a stack works well
    open = util.Stack()
    open.push((problem.getStartState(), " ",0, [] ))
    
    #Make a closed list so we know which states not to check
    closed = []
    
    #Go on till the open list is empty
    while( not open.isEmpty()):
    
        #Take the first element of the list
        state = open.pop()
        
        #Check if that element is the goal state, if so return a path from start to goal
        if(problem.isGoalState(state[0])):
            li = state[3][:]
            li.append(state[1]) 
            return li[1:]

        #Generate the element's successors
        successors =  problem.getSuccessors(state[0])
        for succ in successors:
            
            #Make the list to that node to save in it
            li = state[3][:]
            li.append(state[1])
            
            #If the element is in the closed list ignore it
            if(succ[0] in closed):
                continue

            #Add it to the open list
            open.push((succ[0],succ[1],succ[2], li ))
        #Add the state to the closed list so we dont check it again
        closed.append(state[0])
    
    
    return []
    

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    
    #Make a queue for the open list for the states we want to check
    #In BFS we always want to search to shortest node path so a queue works
    open = util.Queue()
    open.push((problem.getStartState(), " ",0, [] ))
    
    #Make a closed list so we know which states not to check
    closed = []
    
    #Go on till the open list is empty
    while( not open.isEmpty()):
    
        #Take the first element of the list
        state = open.pop()
        
        #Check if that element is the goal state, if so return a path from start to goal
        if(problem.isGoalState(state[0])):
            li = state[3][:]
            li.append(state[1]) 
            return li[1:]

        #Generate the element's successors
        successors =  problem.getSuccessors(state[0])
        for succ in successors:
            
            #Make the list to that node to save in it
            li = state[3][:]
            li.append(state[1])
        
            #If the element is in the closed list ignore it
            if(succ[0] in closed):
                continue
            #Difference between DFS and BFS add the successor to the closed list as well
            #because if a node has already been found onces we dont want to check it again
            closed.append(succ[0])

            #Add it to the open list
            open.push((succ[0],succ[1],succ[2], li ))
        #Add the state to the closed list so we dont check it again
        closed.append(state[0])
    
    
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""

    #Make a PriorityQueue for the open list for the states we want to check
    #In UCS we always want to check the cheepest node
    open = util.PriorityQueue()
    open.push((problem.getStartState(), " ",0, [] ),1)
    
    #Make a closed list so we know which states not to check
    closed = []
    
    #Go on till the open list is empty
    while( not open.isEmpty()):
    
        #Take the first element of the list
        
        state = open.pop()
       
        #Check if that element is the goal state, if so return a path from start to goal
        if(problem.isGoalState(state[0])):
            li = state[3][:]
            li.append(state[1]) 
            return li[1:]
        
        #If the state is not in the closed list go through its successors
        if state[0] not in closed:
            #Add the state to the closed list so we dont check it again
            closed.append(state[0])
            #Generate the element's successors
            successors =  problem.getSuccessors(state[0])
            
            #Make the list to that node to save in it
            #closed.append(succ[0])
            li = state[3][:]
            li.append(state[1])

            for succ in successors:
            #If the element is in the closed list ignore it
                if(succ[0] in closed):
                    continue
                #Add it to the open list
                open.push((succ[0],succ[1],succ[2], li ), succ[2] + problem.getCostOfActions(li[1:]))

    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    #Make a PriorityQueue for the open list for the states we want to check
    #In Astar we always want to check the cheepest node
    #The cost is the Heuristic added to the cost to get to that point from UCS
    open = util.PriorityQueue()
    open.push((problem.getStartState(), " ",0, [] ),1)
    
    #Make a closed list so we know which states not to check
    closed = []
    
    #Go on till the open list is empty
    while( not open.isEmpty()):
        #Take the first element of the list  
        state = open.pop()
       
        #Check if that element is the goal state, if so return a path from start to goal
        if(problem.isGoalState(state[0])):
            li = state[3][:]
            li.append(state[1]) 
            return li[1:]
        
        #If the state is not in the closed list go through its successors
        if state[0] not in closed:
            #Add it to closed so we dont check it again
            closed.append(state[0])
            #Generate the element's successors
            successors =  problem.getSuccessors(state[0])
            
            #Make the path to that node to save in it
            li = state[3][:]
            li.append(state[1])

            for succ in successors:
                #If the element is in the closed list ignore it
                if(succ[0] in closed):
                    continue
                #Add it to the open list
                open.push((succ[0],succ[1],succ[2], li ), heuristic(succ[0], problem) + succ[2] + problem.getCostOfActions(li[1:]))

    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

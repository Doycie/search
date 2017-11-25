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

def searchWithDatastruct2(problem, option):

    #Option specifies which datastructer to use
    if(option == 0):
        open = util.Stack()
    elif(option == 1):
        open = util.Queue()
   
    #Init an open list for all the states we are going to search
    open.push((problem.getStartState(), " ",0, [] ))
    closed = []
    
    #Go on till the open list is empty
    while( not open.isEmpty()):
    
        #Take element of the list
        state = open.pop()
        
        #Check if that element is the goal state, if so return a path from start to goal
        if(problem.isGoalState(state[0])):
            li = state[3][:]
            li.append(state[1])
            return li[1:]
        
        #Generate the element's successors
        successors =  problem.getSuccessors(state[0])
        print state
        
        #If the element is not in the closed list we can add its successors 
        if(state[0] not in closed):
            #Add the element to the closed list
            closed.append(state[0])
            for succ in successors:
                if (succ[0] not in closed): 
                    li = state[3][:]
                    li.append(state[1])
                    open.push((succ[0],succ[1],succ[2], li ))

#OLD SEARCH FUNCTION
def searchWithDatastruct(problem, option):

    if(option == 0):
        open = util.Stack()
    elif(option == 1):
        open = util.Queue()
    #elif(option == 2):
        #open = util.PriorityQueueWithFunction(lambda getCostOfActions)

    open.push((problem.getStartState(), "Stop",0,None ))
    closed = []
    final = []
    while( not open.isEmpty()):
        state = open.pop()
        
   
        
        if(problem.isGoalState(state[0])):
            tempstate = state[3]
            final.append(state[1])
         
            while(not tempstate == None ):
                final.append(tempstate[1])
                tempstate = tempstate[3]
                
                
           
            return (list(reversed(final)))[1:]
             
        successors =  problem.getSuccessors(state[0])
        print successors
        for succ in successors:
            if succ[0] not in closed:
                closed.append(succ[0])
                open.push((succ[0],succ[1],succ[2],state))


    
    
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
    
    return searchWithDatastruct2(problem,0) #Search with Sack
    util.raiseNotDefined()
    

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    return searchWithDatastruct2(problem,1) #Seach with Queue
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    
    
    open = util.PriorityQueue()
    open.push((problem.getStartState(), "Stop",0,None,0 ),0 )
    closed = []
    final = []
    while( not open.isEmpty()):
        state = open.pop()

        if(problem.isGoalState(state[0])):
            tempstate = state[3]
            final.append(state[1])
            while(not tempstate == None ):
                final.append(tempstate[1])
                tempstate = tempstate[3]
            
            return (list(reversed(final)))
             
        successors =  problem.getSuccessors(state[0])
        
        for succ in successors:
            if succ[0] not in closed:
                closed.append(succ[0])
                open.push((succ[0],succ[1],succ[2],state, state[2] + state[4] ), state[2] + state[4] )
    
    
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

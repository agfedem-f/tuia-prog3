from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

def heuristic(state, end):
    return abs(state[0]-end[0]) + abs(state[1]- end[1])

class GreedyBestFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Greedy Best First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost

        # Initialize frontier with the root node
        frontier = PriorityQueueFrontier()
        frontier.add(root, priority=heuristic(root.state, grid.end))

        while True:
            #Check empty
            if frontier.is_empty():
                return NoSolution(reached)
            
            #Remove next node from frontier
            node= frontier.pop()

            #Expand node
            for action in grid.actions(node.state):

                #Get the successor
                successor = grid.result(node.state, action)

                #Check if the succesor was already reached
                if successor in reached:
                    continue

                #Initialize the son node
                son = Node("",successor,cost=node.cost + grid.individual_cost(node.state, action), parent= node, action=action)
                #Mark the successor as reached
                reached[successor]= True

                #Aplly objetive test
                if grid.objective_test(successor):
                    return Solution(son, reached)
                
                #Add son to frontier
                frontier.add(son, priority=heuristic(successor, grid.end))

        return NoSolution(reached)

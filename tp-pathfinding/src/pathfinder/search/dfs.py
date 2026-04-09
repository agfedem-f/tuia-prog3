from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize expanded with the empty dictionary
        expanded = dict()
        #Initialize frontier (stack)
        frontier = StackFrontier()
        frontier.add(root)

        while not frontier.is_empty(): 
            node = frontier.remove() 

            if node.state in expanded:
                continue
            
            expanded[node.state] = True

            
            for action in grid.actions(node.state): 
                
                
                successor_state = grid.result(node.state, action) 
                
                if successor_state not in expanded:
                    
                    cost = node.cost + grid.individual_cost(node.state, action) 
                    son = Node("", successor_state, cost, node, action) 
                    
                    if grid.objective_test(successor_state): 
                        return Solution(son, expanded) 
                    
                    frontier.add(son) 

        return NoSolution(expanded) 
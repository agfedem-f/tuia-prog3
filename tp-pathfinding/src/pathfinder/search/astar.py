from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

def h(state, goal):
    """
    Funcion auxiliar que nos ayuda a calcular la heuristica
    """
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])

class AStarSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using A* Search

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
        frontier.add(root, priority=h(root.state, grid.end))

        while not frontier.is_empty():
            node = frontier.pop()

            if grid.objective_test(node.state):
                return Solution(node, reached)
            
            for action in grid.actions(node.state):
                successor_state = grid.result(node.state, action)

                new_g = node.cost + grid.individual_cost(node.state, action)

                if successor_state not in reached or new_g < reached[successor_state]:
                    reached[successor_state] = new_g
                    son = Node("", successor_state, new_g, node, action)

                    f_value = new_g + h(successor_state, grid.end)
                    frontier.add(son, priority=f_value)
        return NoSolution(reached)

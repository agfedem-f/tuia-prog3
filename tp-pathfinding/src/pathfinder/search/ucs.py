from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

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
        frontier.add(root, priority=0)

        while not frontier.is_empty():
            node = frontier.pop()

            #objetive test
            if grid.objective_test(node.state):
                return Solution(node, reached)
            
            for action in grid.actions(node.state):
                son_state = grid.result(node.state, action)

                new_cost = node.cost + grid.individual_cost(node.state, action)

                if son_state not in reached or new_cost < reached[son_state]:
                    reached[son_state] = new_cost
                    son = Node("", son_state, new_cost, node, action)
                    frontier.add(son, priority=new_cost)
        return NoSolution(reached)

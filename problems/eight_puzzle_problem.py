# Enable the filesystem to access the parent directory and specific subdirectories.
import sys
sys.path.append('../')  # Add the parent directory to the system path for module imports.

# Import essential classes and functions required to work with the search problem.
from init import Problem, Node, cutoff, failure  # Import classes and constants for search problems.

# Import the hamming_distance function from the utility module.
from utility import hamming_distance

# Define the EightPuzzle class, inheriting from the Problem class.
class EightPuzzle(Problem):
    """
    Represents the 8-puzzle problem as a subclass of the generic Problem class.
    
    The puzzle consists of a 3x3 grid with tiles numbered 1 to 8 and one blank space.
    The goal is to rearrange the tiles to match a given goal configuration.
    """
    
    def __init__(self, initial, goal=(0, 1, 2, 3, 4, 5, 6, 7, 8)):
        """
        Initialize the puzzle with an initial state and a goal state.
        
        Args:
            initial: A tuple representing the starting state of the puzzle.
            goal: A tuple representing the goal state (default is the ordered configuration).
        """
        self.initial = initial  # Set the initial state of the puzzle.
        self.goal = goal  # Set the goal state of the puzzle.

    def actions(self, state):
        """
        Return the possible actions given a state.
        
        Args:
            state: A tuple representing the current state of the puzzle.
            
        Returns:
            A tuple of indices representing positions where the blank tile (0) can move.
        """
        # Possible moves for each tile index in the 3x3 grid.
        moves = ((1, 3), (0, 2, 4), (1, 5),
                 (0, 4, 6), (3, 1, 5, 7), (2, 4, 8),
                 (3, 7), (4, 6, 8), (5, 7))
        
        blank = state.index(0)  # Find the index of the blank tile (0).
        return moves[blank]  # Return the possible moves for the current position of the blank tile.

    def result(self, state, action):
        """
        Perform the given action on a state, resulting in a new state.
        
        Args:
            state: A tuple representing the current state of the puzzle.
            action: An index where the blank tile (0) will be moved.
            
        Returns:
            A new tuple representing the state after the move.
        """
        s = list(state)  # Convert the state tuple to a list for mutability.
        blank = state.index(0)  # Find the index of the blank tile (0).
        s[action], s[blank] = s[blank], s[action]  # Swap the blank tile with the tile at the action index.
        return tuple(s)  # Convert the list back to a tuple and return it.
    
    # Define the heuristic function as a method of a class.
    def h(self, node):
        """
        Heuristic function for estimating the cost to reach the goal from the given node.
        
        This heuristic calculates the Hamming distance between the current state of the node
        and the goal state, which represents the number of differing positions between them.
        
        Args:
            node: A Node object representing a state in the search tree.
            
        Returns:
            An integer representing the Hamming distance between the node's state and the goal state.
        """
        # Return the Hamming distance between the current node's state and the goal state.
        return hamming_distance(node.state, self.goal)
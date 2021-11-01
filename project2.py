"""
Math 560
Project 2
Fall 2021

project2.py

Partner 1: QiangQiang Liu
Partner 2: Zelin Jin
Date: 11/01/2021
"""

# Import math and other p2 files.
import math
from p2tests import *

"""
BFS/DFS function

INPUTS
maze: A Maze object representing the maze.
alg:  A string that is either 'BFS' or 'DFS'.

OUTPUTS
path: The path from maze.start to maze.exit.
"""

"""
find_path function

INPUTS
struct: The target struct to store the values.
maze: A Maze object representing the maze.

Functionality: Find the path of the maze by using the given struct and setting the prev parameter for nodes on path.
"""
def find_path(struct, maze):
    # Find the neighbours of start node and push it to struct.
    for vertex_t in maze.start.neigh:
        vertex_t.dist = 1
        vertex_t.prev = maze.start
        struct.push(vertex_t)

    # Keep doing operations on nodes until the struct is empty.
    while not struct.isEmpty():
        # Take out the given node.
        current = struct.pop()
        # Traverse the neighbours for the current node.
        for vertex_t in current.neigh:
            # If current distance is smaller than the stored value, renew the path and push this node into the struct.
            if vertex_t.dist > current.dist + 1:
                vertex_t.dist = current.dist + 1
                # The prev node is set to current node because the current distance is smaller.
                vertex_t.prev = current
                struct.push(vertex_t)

def bdfs(maze, alg):
    # If the alg is not BFS or DFS, raise exception.
    if (alg != 'BFS') and (alg != 'DFS'):
        raise Exception('Incorrect alg! Need BFS or DFS!')

    # Initialization. Set distance to start point to infinity, previous node to null and flag visited to false.
    for i in range(0, len(maze.maze) * len(maze.maze[0])):
        maze.adjList[i].dist = math.inf
        maze.adjList[i].prev = None
        maze.adjList[i].visited = False
    # Renew the parameters for the start node.
    res = []
    maze.start.dist = 0
    maze.start.visited = True
    # if the alg is DFS, create a new stack and call the function find_path.
    if alg == 'DFS':
        stack = Stack()
        find_path(stack, maze)

    # If the alg is BFS, create a new queue nad call the function find_path.
    if alg == 'BFS':
        queue = Queue()
        find_path(queue, maze)

    # Create a temp pointer and set it to exit node.
    temp = maze.exit
    # Find the path by storing the rank for each node into a list.
    while temp is not None:
        res.append(temp.rank)
        temp = temp.prev
    # Return the reversed list.
    return res[::-1]

"""
Main function.
"""
if __name__ == "__main__":
    testMazes(True)

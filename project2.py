"""
Math 560
Project 2
Fall 2021

project2.py

Partner 1:
Partner 2:
Date:
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


def bdfs(maze, alg):
    # If the alg is not BFS or DFS, raise exception.
    if (alg != 'BFS') and (alg != 'DFS'):
        raise Exception('Incorrect alg! Need BFS or DFS!')

    ##### Your implementation goes here. #####
    # Initialization
    for i in range(0, len(maze.maze) * len(maze.maze[0])):
        maze.adjList[i].dist = math.inf
        maze.adjList[i].prev = None
        maze.adjList[i].visited = False

    res = []
    if alg == 'DFS':
        stack = Stack()
        maze.start.dist = 0
        maze.start.visited = True
        for vertex_t in maze.start.neigh:
            # vertex_t.visited = True
            vertex_t.dist = 1
            vertex_t.prev = maze.start
            stack.push(vertex_t)

        while not stack.isEmpty():
            current = stack.pop()
            for vertex_t in current.neigh:
                if vertex_t.dist > current.dist + 1:
                    vertex_t.dist = current.dist + 1
                    vertex_t.prev = current
                    # vertex_t.visited = True
                    stack.push(vertex_t)

        temp = maze.exit
        while temp is not None:
            res.append(temp.rank)
            temp = temp.prev
    return res[::-1]
    ##### Your implementation goes here. #####


"""
Main function.
"""
if __name__ == "__main__":
    testMazes(False)

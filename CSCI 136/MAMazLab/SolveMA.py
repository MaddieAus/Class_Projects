# Madison Austin
# CSCI 136 5/2/25
# QueueOfPositions

import sys
from Maze import Maze
from Position import Position
from StackOfPositionsMA import StackOfPositions
from QueueOfPositionMA import QueueOfPositions
import StdDraw

# Colors for DFS and BFS
from color import RED, BOOK_LIGHT_BLUE, DARK_RED, LIGHT_GRAY

# Helper to add neighbors to data structure
def get_neighbors(maze, pos):
    neighbors = []
    x, y = pos.getX(), pos.getY()

    if maze.openNorth(pos):
        neighbors.append(Position(x, y + 1))
    if maze.openSouth(pos):
        neighbors.append(Position(x, y - 1))
    if maze.openEast(pos):
        neighbors.append(Position(x + 1, y))
    if maze.openWest(pos):
        neighbors.append(Position(x - 1, y))

    return neighbors

# DFS using Stack
def solve_with_stack(maze):
    stack = StackOfPositions()
    count = 0
    start = maze.getStart()
    finish = maze.getFinish()
    stack.push(start)
    maze.setVisited(start)

    while not stack.isEmpty():
        current = stack.pop()
        current.draw(RED)
        StdDraw.show(20)

        if current.equals(finish):
            break

        for neighbor in get_neighbors(maze, current):
            if not maze.isVisited(neighbor):
                stack.push(neighbor)
                maze.setVisited(neighbor)
                neighbor.draw(BOOK_LIGHT_BLUE)
                StdDraw.show(10)
                count += 1

    return count

# BFS using Queue
def solve_with_queue(maze):
    queue = QueueOfPositions()
    count = 0
    start = maze.getStart()
    finish = maze.getFinish()
    queue.enqueue(start)
    maze.setVisited(start)

    while not queue.isEmpty():
        current = queue.dequeue()
        current.draw(DARK_RED)
        StdDraw.show(20)

        if current.equals(finish):
            break

        for neighbor in get_neighbors(maze, current):
            if not maze.isVisited(neighbor):
                queue.enqueue(neighbor)
                maze.setVisited(neighbor)
                neighbor.draw(LIGHT_GRAY)
                StdDraw.show(10)
                count += 1

    return count

# Main entry
def main():
    if len(sys.argv) < 2:
        print("Usage: python Solve.py <maze_size>")
        return

    n = int(sys.argv[1])
    maze = Maze(n)
    maze.draw()

    print("Solving with stack (DFS)...")
    count_stack = solve_with_stack(maze)
    print("Positions visited (stack):", count_stack)

    maze.clear()
    maze.draw()

    print("Solving with queue (BFS)...")
    count_queue = solve_with_queue(maze)
    print("Positions visited (queue):", count_queue)

if __name__ == "__main__":
    main()

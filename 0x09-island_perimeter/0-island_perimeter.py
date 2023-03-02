#!/usr/bin/python3
"""
Contains the function 'island_perimeter'
"""

def island_perimeter(grid):
    """ Retruns the perimeter of the island described in grid
    
        -- grid is a list of list of integers:
            - 0 represents water
            - 1 represents land
            - Each cell is square, with a side length of 1
            - Cells are connected horizontally/vertically (not diagonally).
            - grid is rectangular, with its width and height not exceeding 100

        -- The grid is completely surrounded by water

        -- There is only one island (or nothing).

        -- The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).
    """
    row = len(grid)
    col = len(grid[0])
    perimeter = 0
    
    r = 0
    while r < row:
        c = 0
        while c < col:
            if grid[r][c] == 1:
                if r == 0 or grid[r-1][c] == 0:
                    perimeter +=1
                if c == 0 or grid[r][c-1] == 0:
                    perimeter +=1
                if r == row - 1 or grid[r+1][c] == 0:
                    perimeter += 1
                if c == col -1 or grid[r][c+1] == 0:
                    perimeter += 1
            c += 1
        r += 1
    return perimeter
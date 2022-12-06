# Link: https://adventofcode.com/2021/day/15
from ..utils import AOCTestCase
import heapq


def get_adjacent(data, i, j):
    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        i1, j1 = i + dy, j + dx
        if 0 <= i1 < len(data) and 0 <= j1 < len(data[0]):
            yield i1, j1


def search(grid, width, height):
    pq = [(0, (0, 0))]
    visited = {(0, 0)}
    while pq:
        dist, (i, j) = heapq.heappop(pq)
        if i == height - 1 and j == width - 1:
            return dist
        for i1, j1 in get_adjacent(grid, i, j):
            if (i1, j1) not in visited:
                heapq.heappush(pq, (dist + grid[i1][j1], (i1, j1)))
                visited.add((i1, j1))

class Chiton(AOCTestCase):
    day = 15
    year = 2021

    def find_in_grid(self, grid) -> int:
        initial = grid[0][0]
        
        height = len(grid)
        width = len(grid[0])

        d = [(1, 0), (0, 1)]

        for row in range(height - 1, -1, -1):
            for column in range(width - 1, -1, -1):
                neighbours = [(row + drow, column + dcolumn) for drow, dcolumn in d if 0 <= row + drow < height and 0 <= column + dcolumn < width]
                if len(neighbours) == 0:
                    continue
                grid[row][column] = min(grid[row][column] + grid[nrow][ncolumn] for nrow, ncolumn in neighbours)
        

        # for row in grid:
        #     for cell in row:
        #         print(str(cell).rjust(2, ' '), end="")
        #     print()
        
        return grid[0][0] - initial

    def part1(self, content: str) -> int:
        grid = self.intmap(content)
        return self.find_in_grid(grid)

    def part2(self, content: str) -> int:
        grid = self.intmap(content)
         
        height = len(grid)
        width = len(grid[0])
        
        new_map = [line * 5 for line in grid * 5]
        for i in range(height * 5):
            for j in range(width * 5):
                new_map[i][j] = (new_map[i][j] + i // height + j // width - 1) % 9 + 1
                
        # print(f"Generated grid is {len(full_grid)}x{len(full_grid[0])}")

        # for row in full_grid:
        #     for cell in row:
        #         print(str(cell).rjust(2, ' '), end="")
        #     print()
        return search(new_map, width * 5, height * 5)
        
        
        


                
        

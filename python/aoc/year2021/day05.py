# Link: https://adventofcode.com/2021/day/5
from typing import List, Tuple
from ..utils import AOCTestCase
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
    
@dataclass
class Line:
    start: Point
    end: Point

class HydrothermalVenture(AOCTestCase):
    day = 5
    year = 2021

    def read(self, content: str) -> List[Line]:
        lines = self.lines(content)
        
        output = []
        for line in lines: 
            startRaw, endRaw= line.split(' -> ')
            x, y = [int(x) for x in startRaw.split(',')]
            start = Point(x, y)
            x, y = [int(x) for x in endRaw.split(',')]
            end = Point(x,y)
            
            output += [Line(start, end)]
        return output

    def find_dimensions(self, lines: List[Line]) -> Tuple[int, int]:
        maxX = max(max(line.start.x, line.end.x) for line in lines)
        maxY = max(max(line.start.y, line.end.y) for line in lines)
        return (maxX, maxY)

    def part1(self, content: str) -> int:
        lines = self.read(content)
        
        for line in lines:
            print(line)
        
        maxX, maxY = self.find_dimensions(lines) 
        
        grid = [[0 for _ in range(maxX+1)] for _ in range(maxY+1)]
        
        for line in lines:
            start, end = line.start, line.end
            if start.x != end.x and start.y != end.y:
                continue

            dx = 1 if end.x > start.x else -1 if end.x < start.x else 0
            dy = 1 if end.y > start.y else -1 if end.y < start.y else 0

            point = Point(start.x, start.y) 
             
            grid[point.y][point.x] += 1
            while point.x != end.x or point.y != end.y:
                point.x += dx 
                point.y += dy 
                grid[point.y][point.x] += 1
                
        for line in grid:
            print(line)

        return sum(1 for row in grid for cell in row if cell > 1)
        

    def part2(self, content: str) -> int:
        lines = self.read(content)
        
        for line in lines:
            print(line)
        
        maxX, maxY = self.find_dimensions(lines) 
        
        grid = [[0 for _ in range(maxX+1)] for _ in range(maxY+1)]
        
        for line in lines:
            start, end = line.start, line.end

            dx = 1 if end.x > start.x else -1 if end.x < start.x else 0
            dy = 1 if end.y > start.y else -1 if end.y < start.y else 0

            point = Point(start.x, start.y) 
             
            grid[point.y][point.x] += 1
            while point.x != end.x or point.y != end.y:
                point.x += dx 
                point.y += dy 
                grid[point.y][point.x] += 1
                
        for line in grid:
            print(line)

        return sum(1 for row in grid for cell in row if cell > 1)

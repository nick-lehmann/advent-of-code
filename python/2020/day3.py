from enum import Enum
from typing import List
from dataclasses import dataclass
from math import prod

@dataclass
class Point:
  x: int = 0
  y: int = 0


Map = List[List[chr]]

def find_trees(map: Map, slope: Point) -> int:
  row = 0
  column = 0
  width = len(map[0])
  trees = 0
  while row < len(map):
    trees += int(map[row][column] == "#")
    row += slope.x
    column = (column + slope.y) % width
  return trees

def part1(map: Map) -> int:
  return find_trees(map, Point(x=1, y=3))
    
def part2(map: Map) -> int:
  points = [
    Point(x=1, y=1),
    Point(x=3, y=1),
    Point(x=5, y=1),
    Point(x=7, y=1),
    Point(x=1, y=2)
  ]
  product = 1
  for point in points:
    product *= find_trees(map, point)
  return product


if __name__ == '__main__':
    with open("../../exercises/2020/03.txt") as file:
        map = []
        for line in file.readlines():
          row = list(line.strip())
          map += [row]
        print(part1(map))
        print(part2(map))
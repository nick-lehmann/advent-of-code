# Link: https://adventofcode.com/2020/day/12
from ..utils import AOCTestCase
from dataclasses import dataclass


@dataclass
class Point:
    x: int = 0
    y: int = 0


moves = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
compass = "NESW"


class RainRisk(AOCTestCase):
    day = 12
    year = 2020

    def part1(self, content: str) -> int:
        point = Point()
        current_direction = 'E'
        for line in self.lines(content):
            action = line[0]
            value = int(line[1:])

            if action in ['R', 'L']:
                turn = (value // 90)
                factor = -1 if action == 'L' else 1
                new_index = (compass.index(
                    current_direction) + factor * turn) % 4
                current_direction = compass[new_index]
                continue

            move = None
            if action == 'F':
                move = moves[current_direction]
            if action in ['N', 'E', 'S', 'W']:
                move = moves[action]

            point.x += value * move[0]
            point.y += value * move[1]

        return abs(point.x) + abs(point.y)

    def part2(self, content: str) -> int:
        waypoint = Point(x=10, y=1)
        ship = Point()

        for line in self.lines(content):
            action = line[0]
            value = int(line[1:])

            if action in ['R', 'L']:
                turn = value // 90
                turn %= 4
                if action == 'L':
                    turn = 4 - turn
                for _ in range(turn):
                    waypoint.x, waypoint.y = waypoint.y, -waypoint.x

            if action == 'F':
                ship.x += value * waypoint.x
                ship.y += value * waypoint.y

            if action in ['N', 'E', 'S', 'W']:
                move = moves[action]
                waypoint.x += value * move[0]
                waypoint.y += value * move[1]

        return abs(ship.x) + abs(ship.y)

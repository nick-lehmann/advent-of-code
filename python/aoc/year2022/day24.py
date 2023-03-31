# Link: https://adventofcode.com/2022/day/24
from dataclasses import dataclass
from ..utils import AOCTestCase
from collections import defaultdict

Direction = tuple[int, int]
Coordinates = tuple[int, int]
Blizzards = dict[Coordinates, list[Direction]]


@dataclass
class Map:
    height: int
    width: int

    start: Coordinates
    end: Coordinates

    players: set[Coordinates]
    blizzards: Blizzards

    def in_bounds(self, row, column) -> bool:
        return (
            (0 < row < self.height - 1 and 0 < column < self.width - 1)
            or (row, column) == self.start
            or (row, column) == self.end
        )

    def print(self):
        """Prints the current state of the blizzard basin."""
        map = []
        map += [["#"] * self.width]
        for _ in range(1, self.height - 1):
            map += [["#"] + ["."] * (self.width - 2) + ["#"]]
        map += [["#"] * self.width]

        for (row, column), directions in self.blizzards.items():
            if len(directions) > 1:
                map[row][column] = str(len(directions))
                continue
            map[row][column] = self.reverseDirectionsMap[directions[0]]

        # Clear start
        startrow, startcolumn = self.start
        map[startrow][startcolumn] = "."

        # Clear end
        endrow, endcolumn = self.end
        map[endrow][endcolumn] = "."

        # Show player
        for row, column in self.players:
            map[row][column] = "E"

        for row in map:
            print("".join(row))


class BlizzardBasin(AOCTestCase):
    day = 24
    year = 2022

    directions: list[Direction] = [(1, 0), (-1, 0), (0, -1), (0, 1), (0, 0)]
    directionsMap: dict[chr, Direction] = {
        ">": (0, 1),
        "<": (0, -1),
        "^": (-1, 0),
        "v": (1, 0),
    }
    reverseDirectionsMap: dict[Direction, chr] = {
        (0, 1): ">",
        (0, -1): "<",
        (-1, 0): "^",
        (1, 0): "v",
    }

    def find_empty(self, line: str) -> int:
        for i, c in enumerate(line):
            if c == ".":
                return i
        raise ValueError("No empty space found")

    def read(self, content) -> Map:
        map = self.map(content)
        height = len(map)
        width = len(map[0])
        start = (0, self.find_empty(map[0]))
        end = (height - 1, self.find_empty(map[height - 1]))

        blizzards = defaultdict(list)
        for row in range(1, height - 1):
            for column in range(1, width - 1):
                cell = map[row][column]
                if cell == ".":
                    continue
                direction = self.directionsMap[cell]
                blizzards[(row, column)] += [direction]

        return Map(height, width, start, end, players=[], blizzards=blizzards)

    def storm(self, blizzards: Blizzards, height: int, width: int) -> Blizzards:
        """Moves the blizzards to the next position."""
        new_blizzards = defaultdict(list)
        for (row, column), directions in blizzards.items():
            for drow, dcolumn in directions:
                new_row = row + drow
                if new_row == 0 or new_row == height - 1:
                    new_row = (new_row + 2 * drow) % height

                new_column = column + dcolumn
                if new_column == 0 or new_column == width - 1:
                    new_column = (new_column + 2 * dcolumn) % width
                new_blizzards[(new_row, new_column)] += [(drow, dcolumn)]
        return new_blizzards

    def search(
        self, map: Map, start: Coordinates, end: Coordinates
    ) -> tuple[int, Blizzards]:
        """Returns the minimum number of rounds (minutes) to reach the end."""
        map.players = {start}
        round = 0
        while True:
            # print(f"Round {round + 1}")
            blizzards = self.storm(map.blizzards, map.height, map.width)
            next_players = set()  # All possible places the player can move to

            for row, column in map.players:
                for drow, dcolumn in self.directions:
                    next_row, next_column = row + drow, column + dcolumn
                    if (next_row, next_column) == end:
                        # Found it
                        return round + 1, map

                    if not map.in_bounds(next_row, next_column):
                        # Would leave the map
                        continue

                    if (next_row, next_column) in blizzards:
                        # Clash with blizzard
                        continue

                    next_players |= {(next_row, next_column)}

            map.players = next_players
            map.blizzards = blizzards
            # self.print(blizzards)

            round += 1

    def part1(self, content: str) -> int:
        map = self.read(content)
        time, map = self.search(map, map.start, map.end)

        return time

    def part2(self, content: str) -> int:
        map = self.read(content)
        start = map.start
        end = map.end

        trip1, map = self.search(map, start, end)
        trip2, map = self.search(map, end, start)
        trip3, map = self.search(map, start, end)

        return trip1 + trip2 + trip3 - 2

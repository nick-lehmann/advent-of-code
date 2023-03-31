# Link: https://adventofcode.com/2021/day/13
from ..utils import AOCTestCase


# Parse sentencnes like "fold along y=7" and return both the direction and the distance
def parse_sentence(line):
    last = line.split(" ")[-1]
    direction, distance = last.split("=")
    return direction, int(distance)


class TransparentOrigami(AOCTestCase):
    day = 13
    year = 2021

    def part1(self, content: str) -> int:
        points, folds = content.strip().split("\n\n")

        points = {tuple(map(int, line.split(","))) for line in points.split("\n")}
        for i, line in enumerate(folds.split("\n")):
            coordinate, n = line.split()[-1].split("=")
            n = int(n)
            for x, y in list(points):
                points.remove((x, y))
                if coordinate == "x" and x > n:
                    x = 2 * n - x

                if coordinate == "y" and y > n:
                    y = 2 * n - y

                points.add((x, y))

            if i == 0:
                return len(points)

        X, Y = zip(*points)
        for y in range(max(Y) + 1):
            for x in range(max(X) + 1):
                print(" #"[(x, y) in points], end="")

            print()

        return 0

    def part2(self, content: str) -> int:
        points, folds = content.strip().split("\n\n")

        points = {tuple(map(int, line.split(","))) for line in points.split("\n")}
        for i, line in enumerate(folds.split("\n")):
            coordinate, n = line.split()[-1].split("=")
            n = int(n)
            for x, y in list(points):
                points.remove((x, y))
                if coordinate == "x" and x > n:
                    x = 2 * n - x

                if coordinate == "y" and y > n:
                    y = 2 * n - y

                points.add((x, y))

        X, Y = zip(*points)
        for y in range(max(Y) + 1):
            for x in range(max(X) + 1):
                print(" #"[(x, y) in points], end="")

            print()

        return 0

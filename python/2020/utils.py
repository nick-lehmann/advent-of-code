import re
from typing import List
import inspect
from dataclasses import dataclass
from pathlib import Path
from unittest import TestCase
import unittest


@dataclass
class AOCDay:
    day: int
    year: int

    @property
    def padded_day(self) -> str:
        return str(self.day).rjust(2, "0")

    @property
    def directory(self) -> Path:
        return Path(f"../../exercises/{self.year}/{self.padded_day}")

    @property
    def puzzle_path(self) -> Path:
        return self.directory / "puzzle.txt"

    @property
    def puzzle_solution1_path(self) -> Path:
        return self.directory / "puzzle_solution1.txt"

    @property
    def puzzle_solution2_path(self) -> Path:
        return self.directory / "puzzle_solution2.txt"

    @property
    def puzzle_example_path(self) -> Path:
        return self.directory / "example.txt"

    @property
    def puzzle_example_solution_path(self) -> Path:
        return self.directory / "example_solution.txt"


class AOCTestCase(TestCase):
    _puzzle_lines: List[str]
    _day: AOCDay

    @classmethod
    def setUpClass(cls):
        if cls is AOCTestCase:
            raise unittest.SkipTest("%s is an abstract base class" % cls.__name__)
        else:
            super(AOCTestCase, cls).setUpClass()

    def setUp(self) -> None:
        self._day = get_aoc_day()
        with open(self._day.puzzle_path) as f:
            self._puzzle_lines = f.readlines()
        return super().setUp()

    @property
    def lines(self) -> List[str]:
        return self._puzzle_lines

    @property
    def ints(self) -> List[int]:
        return [int(line.strip()) for line in self._puzzle_lines]

    @property
    def ints_set(self) -> List[int]:
        return {int(line.strip()) for line in self._puzzle_lines}

    @property
    def floats_set(self) -> List[int]:
        return {float(line.strip()) for line in self._puzzle_lines}

    @property
    def puzzle_solution1(self) -> int:
        with open(self._day.puzzle_solution1_path) as f:
            return int(f.readline().strip("\n"))

    @property
    def puzzle_solution2(self) -> int:
        with open(self._day.puzzle_solution2_path) as f:
            return int(f.readline().strip("\n"))

    # Override in concrete test case
    def part1(self) -> int:
        pass

    # Override in concrete test case
    def part2(self) -> int:
        pass

    def test_part1(self):
        result = self.part1()
        solution = self.puzzle_solution1
        self.assertEqual(result, solution)

    def test_part2(self):
        result = self.part2()
        solution = self.puzzle_solution2
        self.assertEqual(result, solution)


def get_aoc_day() -> AOCDay:
    filename = inspect.stack()[-1].filename
    match = re.search(r".*/(\d+)/day(\d+)\.py", filename)
    return AOCDay(year=int(match.group(1)), day=int(match.group(2)))

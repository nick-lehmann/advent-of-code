import os
import re
from typing import List
import inspect
from dataclasses import dataclass
from pathlib import Path
from unittest import TestCase
import unittest
from enum import Enum


@dataclass
class AOCDay:
    day: int
    year: int

    @property
    def paddedday(self) -> str:
        return str(self.day).rjust(2, "0")

    @property
    def directory(self) -> Path:
        return Path(f"../../exercises/{self.year}/{self.paddedday}")

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
    def puzzle_example_solution1_path(self) -> Path:
        return self.directory / "example_solution1.txt"

    @property
    def puzzle_example_solution2_path(self) -> Path:
        return self.directory / "example_solution2.txt"


class AOCTestCase(TestCase):
    _puzzle_lines: List[str]
    _mode: str

    @classmethod
    def setUpClass(cls):
        if cls is AOCTestCase:
            raise unittest.SkipTest("%s is an abstract base class" % cls.__name__)
        else:
            super(AOCTestCase, cls).setUpClass()

    def setUp(self) -> None:
        with open(self.day.puzzle_path) as f:
            self._puzzle_lines = f.readlines()

        self._mode = os.environ.get("MODE", "prod")
        return super().setUp()

    @property
    def day(self) -> AOCDay:
        filename = inspect.stack()[-1].filename
        match = re.search(r".*/(\d+)/day(\d+)\.py", filename)
        return AOCDay(year=int(match.group(1)), day=int(match.group(2)))

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
    def map(self) -> List[List[chr]]:
        map = []
        for line in self.lines:
            row = list(line.strip())
            map += [row]
        return map

    @property
    def example_solution1(self) -> int:
        with open(self.day.puzzle_example_solution1_path) as f:
            return int(f.readline().strip("\n"))

    @property
    def example_solution2(self) -> int:
        with open(self.day.puzzle_example_solution2_path) as f:
            return int(f.readline().strip("\n"))

    @property
    def puzzle_solution1(self) -> int:
        with open(self.day.puzzle_solution1_path) as f:
            return int(f.readline().strip("\n"))

    @property
    def puzzle_solution2(self) -> int:
        with open(self.day.puzzle_solution2_path) as f:
            return int(f.readline().strip("\n"))

    @property
    def solution1(self) -> int:
        if self._mode == "prod":
            return self.puzzle_solution1
        return self.example_solution1

    @property
    def solution2(self) -> int:
        if self._mode == "prod":
            return self.puzzle_solution2
        return self.example_solution2

    # Override in concrete test case
    def part1(self) -> int:
        pass

    # Override in concrete test case
    def part2(self) -> int:
        pass

    def test_part1(self):
        result = self.part1()
        solution = self.solution1
        self.assertEqual(result, solution)

    def test_part2(self):
        result = self.part2()
        solution = self.solution2
        self.assertEqual(result, solution)

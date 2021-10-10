import os
import unittest
from typing import List, Set
from unittest import TestCase
from .exercise import AOCFile, Exercise


class AOCTestCase(TestCase):
    day: int
    year: int
    exercise: Exercise
    _mode: str

    def __init__(self, *args, **kwargs):
        try:
            self.exercise = Exercise(self.day, self.year)
        except:
            pass
        return super().__init__(*args, **kwargs)

    @classmethod
    def setUpClass(cls):
        if cls is AOCTestCase:
            raise unittest.SkipTest("%s is an abstract base class" % cls.__name__)
        else:
            super(AOCTestCase, cls).setUpClass()

    def setUp(self) -> None:
        self._mode = os.environ.get("MODE", "prod")
        return super().setUp()

    def lines(self, content: str) -> List[str]:
        lines = content.split("\n")
        if lines[-1] == "":
            return lines[:-1]
        return lines

    def blocks(self, content: str) -> List[str]:
        return content.split("\n\n")

    def ints(self, content: str) -> List[int]:
        return [int(line.strip()) for line in self.lines(content)]

    def ints_set(self, content: str) -> Set[int]:
        return {int(line.strip()) for line in self.lines(content)}

    def floats_set(self, content: str) -> Set[int]:
        return {float(line.strip()) for line in self.lines(content)}

    def map(self, content: str) -> List[List[chr]]:
        map = []
        for line in self.lines(content):
            row = list(line.strip())
            map += [row]
        return map

    # Override in concrete test case
    def part1(self, content: str) -> int:
        pass

    # Override in concrete test case
    def part2(self, content: str) -> int:
        pass

    def test_part1(self):
        try:
            input = self.exercise.get_task(AOCFile.Example)
            solution = self.exercise.get_solution(AOCFile.ExampleSolution1)
            result = self.part1(input)
            self.assertEqual(result, solution)
        except RuntimeError:
            raise unittest.SkipTest("No example found for this test")

        try:
            input = self.exercise.get_task(AOCFile.Puzzle)
            solution = self.exercise.get_solution(AOCFile.PuzzleSolution1)
            result = self.part1(input)
            self.assertEqual(result, solution)
        except RuntimeError:
            raise unittest.SkipTest("No task found for this test")

    def test_part2(self):
        try:
            input = self.exercise.get_task(AOCFile.Example)
            solution = self.exercise.get_solution(AOCFile.ExampleSolution2)
        except RuntimeError:
            raise unittest.SkipTest("No example found for this test")

        result = self.part2(input)
        self.assertEqual(result, solution)

        try:
            input = self.exercise.get_task(AOCFile.Puzzle)
            solution = self.exercise.get_solution(AOCFile.PuzzleSolution2)
        except RuntimeError:
            raise unittest.SkipTest("No task found for this test")

        result = self.part2(input)
        self.assertEqual(result, solution)

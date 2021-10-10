from dataclasses import dataclass
from pathlib import Path
from typing import List, Set
from enum import Enum
from pathlib import Path


class AOCMode(Enum):
    Solving = 1
    Verifying = 2


class AOCFile(Enum):
    Puzzle = "puzzle.txt"
    Example = "example.txt"
    PuzzleSolution1 = "puzzle_solution1.txt"
    PuzzleSolution2 = "puzzle_solution2.txt"
    ExampleSolution1 = "example_solution1.txt"
    ExampleSolution2 = "example_solution2.txt"


@dataclass
class Exercise:
    day: int
    year: int

    @property
    def paddedday(self) -> str:
        return str(self.day).rjust(2, "0")

    @property
    def base(self) -> Path:
        return Path(f"../exercises/{self.year}/{self.paddedday}")

    def get_task(self, file: AOCFile) -> str:
        path: Path = self.base / file.value
        if not path.exists():
            raise RuntimeError(f"File {file.value} does not exist")

        with open(path) as f:
            content = f.read()

        if content == "":
            raise RuntimeError(f"File {file.value} is empty")

        return content

    def get_solution(self, solution: AOCFile) -> int:
        line = self.get_task(solution)
        return int(line)

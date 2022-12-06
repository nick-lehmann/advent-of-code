from pathlib import Path
import yaml
import unittest
from unittest import TestCase

from .inputs import InputMixin


class AOCTestCase(TestCase, InputMixin):
    day: int
    year: int

    @classmethod
    def setUpClass(cls):
        if cls is AOCTestCase:
            raise unittest.SkipTest("%s is an abstract base class" % cls.__name__)
        else:
            super(AOCTestCase, cls).setUpClass()

    @property
    def aoc(self):
        path = Path(f"../exercises/{self.year}/{self.paddedday}.yaml")
        with open(path) as f:
            return yaml.safe_load(f)

    def test(self):
        config = self.aoc
        for test_name, test_config in config["tests"].items():
            for i in range(len(test_config)):
                print(f"Testing {test_name}")
                input = test_config[i]["input"]
                solution = test_config[i]["solution"]

                result = str(getattr(self, test_name)(input))
                self.assertEqual(result, solution)

    def part1(self, content: str) -> int:
        pass

    def part2(self, content: str) -> int:
        pass

    @property
    def paddedday(self) -> str:
        return str(self.day).rjust(2, "0")

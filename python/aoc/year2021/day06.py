# Link: https://adventofcode.com/2021/day/6
from ..utils import AOCTestCase
from collections import defaultdict


class Lanternfish(AOCTestCase):
    day = 6
    year = 2021

    def read(self, content: str) -> list[int]:
        return [int(x) for x in content.strip().split(",")]

    def make_counter(self, fishes: list[int]) -> list[int]:
        counter = [0] * 9
        for fish in fishes:
            counter[fish] += 1
        return counter

    def play_naive(self, fishes: list[int], rounds: int) -> int:
        for round in range(rounds):
            print(len(fishes))
            new_fishes = []
            for fish in fishes:
                if fish == 0:
                    new_fishes += [6, 8]
                else:
                    new_fishes += [fish - 1]
            fishes = new_fishes
        return len(fishes)

    def play_clever(self, fishes: list[int], rounds: int):
        for round in range(rounds):
            print(f"Simulating round {round}")
            new_fishes = [0] * 9

            for age, count in enumerate(fishes):
                if age == 0:
                    new_fishes[6] += count
                    new_fishes[8] += count
                else:
                    new_fishes[age - 1] += count

            fishes = new_fishes

        return sum(fishes)

    def part1(self, content: str) -> int:
        fishes = self.read(content)
        naive_answer = self.play_naive(fishes, 80)
        print("Naive answer: ", naive_answer)

        counter = self.make_counter(fishes)
        clever_answer = self.play_clever(counter, 80)
        print("Clever answer: ", clever_answer)
        return clever_answer

    def part2(self, content: str) -> int:
        fishes = self.read(content)
        naive_answer = self.play_naive(fishes, 256)
        print("Naive answer: ", naive_answer)

        counter = self.make_counter(fishes)
        clever_answer = self.play_clever(counter, 256)
        print("Clever answer: ", clever_answer)
        return clever_answer

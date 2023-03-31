# Link: https://adventofcode.com/2021/day/14
from ..utils import AOCTestCase
from collections import Counter


class ExtendedPolymerization(AOCTestCase):
    day = 14
    year = 2021

    def read(self, content: str):
        template, rawRules = content.split("\n\n")
        rules = {}
        for line in self.lines(rawRules):
            pattern, sub = line.split(" -> ")
            rules[pattern] = sub

        return template, rules

    def play(self, content: str, rounds: int) -> int:
        template, rules = self.read(content)

        counter = Counter()
        for i in range(len(template) - 1):
            part = template[i : i + 2]
            counter[part] += 1

        for round in range(1, rounds + 1):
            next_counter = Counter()
            for part, count in counter.items():
                if part not in rules or count == 0:
                    continue

                sub = rules[part]
                part1 = part[0] + sub
                part2 = sub + part[1]
                next_counter[part1] += count
                next_counter[part2] += count

            counter = next_counter
            print(f"Round {round}: {counter.most_common()}")

        letter_counter = Counter()
        for part, count in counter.most_common():
            letter_counter[part[0]] += count
            letter_counter[part[1]] += count

        rank = letter_counter.most_common()

        def correct(letter, count):
            count = count // 2
            if letter in [template[0], template[-1]]:
                count += 1
            return count

        print(f"Rank: {rank}")
        most_common = correct(*rank[0])
        least_common = correct(*rank[-1])
        return most_common - least_common

    def part1(self, content: str) -> int:
        return self.play(content, 10)

    def part2(self, content: str) -> int:
        return self.play(content, 40)

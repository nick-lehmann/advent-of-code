# Link: https://adventofcode.com/2021/day/10
from ..utils import AOCTestCase


class SyntaxScoring(AOCTestCase):
    day = 10
    year = 2021

    opening_brackets = {")": "(", "}": "{", "]": "[", ">": "<"}

    scores = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }

    autocomplete_scores = {
        "(": 1,
        "[": 2,
        "{": 3,
        "<": 4,
    }

    def part1(self, content: str) -> int:
        lines = self.lines(content)

        score = 0

        for lineIndex, line in enumerate(lines):
            stack = []
            for char in line:
                if char in self.opening_brackets:
                    if stack[-1] == self.opening_brackets[char]:
                        stack.pop()
                    else:
                        score += self.scores[char]
                        print(f"{lineIndex + 1} {char} {score}")
                        break
                elif char in self.opening_brackets.values():
                    stack.append(char)

        return score

    def part2(self, content: str) -> int:
        lines = self.lines(content)

        scores = []

        for lineIndex, line in enumerate(lines):
            stack = []
            for char in line:
                if char in self.opening_brackets:
                    if stack[-1] == self.opening_brackets[char]:
                        stack.pop()
                    else:
                        break
                elif char in self.opening_brackets.values():
                    stack.append(char)
            else:
                score = 0
                for char in reversed(stack):
                    score *= 5
                    score += self.autocomplete_scores[char]
                    print(f"{lineIndex + 1} {char} {score}")
                scores += [score]

        scores.sort()
        return scores[len(scores) // 2]

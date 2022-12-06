# Link: https://adventofcode.com/2022/day/02
from ..utils import AOCTestCase
from enum import Enum


class Choice(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3


value = {Choice.Rock: 1, Choice.Paper: 2, Choice.Scissors: 3}

win = {
    Choice.Rock: Choice.Scissors,
    Choice.Paper: Choice.Rock,
    Choice.Scissors: Choice.Paper,
}


class RockPaperScissors(AOCTestCase):
    day = 2
    year = 2022

    def part1(self, content: str) -> int:
        lines = filter(bool, content.split("\n"))
        score = 0
        for line in lines:
            (input1, input2) = line.split(" ")

            player1 = {
                "A": Choice.Rock,
                "B": Choice.Paper,
                "C": Choice.Scissors,
            }[input1]

            player2 = {
                "X": Choice.Rock,
                "Y": Choice.Paper,
                "Z": Choice.Scissors,
            }[input2]

            if player1 == player2:
                # Draw
                score += 3

            if win[player2] == player1:
                # Win
                score += 6

            score += value[player2]

        return score

    def part2(self, content: str) -> int:
        lines = filter(bool, content.split("\n"))
        score = 0
        for line in lines:
            (input1, input2) = line.split(" ")

            player1 = {
                "A": Choice.Rock,
                "B": Choice.Paper,
                "C": Choice.Scissors,
            }[input1]

            diff = {
                "X": -1,
                "Y": 0,
                "Z": 1,
            }[input2]

            choices = [Choice.Rock, Choice.Paper, Choice.Scissors]
            my_choice = choices[(choices.index(player1) + diff) % 3]

            end = {
                "X": 0,
                "Y": 1,
                "Z": 2,
            }[input2]

            roundScore = 3 * end + value[my_choice]
            print(f"{input1} {input2} {roundScore}")
            score += roundScore

        print(f"Total score of {score}")
        return score

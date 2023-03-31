# Link: https://adventofcode.com/2021/day/21
from typing import List, Tuple
from ..utils import AOCTestCase
from dataclasses import dataclass
from functools import lru_cache


@dataclass
class Player:
    number: int
    position: int
    score: int = 0


ROLLS_PER_ROUND = 3


class DiracDice(AOCTestCase):
    day = 21
    year = 2021

    def read(self, content) -> List[Player]:
        return [
            Player(index + 1, int(line.split()[-1]))
            for index, line in enumerate(self.lines(content))
        ]

    def part1(self, content: str) -> int:
        players = self.read(content)
        next_dice = 1
        total_dice_rolls = 0

        print(players)
        while True:
            for player in players:
                throws = list(range(next_dice, next_dice + ROLLS_PER_ROUND))
                next_dice += ROLLS_PER_ROUND
                total_dice_rolls += ROLLS_PER_ROUND

                advance = sum(throws)

                new_position = player.position + advance
                while new_position > 10:
                    new_position -= 10

                player.position = new_position
                player.score += new_position

                print(
                    f"Player {player.number} rolls {throws} and moves to space {player.position} for a total score of {player.score}."
                )

                if player.score >= 1000:
                    other_player = next(o for o in players if o is not player)
                    print(
                        f"Done. Total dice rolls: {total_dice_rolls}; other player score: {other_player.score}"
                    )
                    return total_dice_rolls * other_player.score

    @lru_cache(maxsize=None)
    def wins(
        self, scores: Tuple[int, int], positions: Tuple[int, int], turn: int
    ) -> Tuple[int, int]:
        if scores[0] >= 21:
            return 1, 0
        if scores[1] >= 21:
            return 0, 1

        wins1, wins2 = 0, 0
        player = turn // 3
        for throw in range(ROLLS_PER_ROUND):
            pos = (positions[player] + throw) % 10 + 1
            score = scores[player] + (turn % 3 == 2 and pos)
            w1, w2 = self.wins(
                (scores[0], score) if player == 1 else (score, scores[1]),
                (positions[0], pos) if player == 1 else (pos, positions[1]),
                (turn + 1) % 6,
            )
            wins1 += w1
            wins2 += w2
        return wins1, wins2

    def part2(self, content: str) -> int:
        players = self.read(content)
        positions = tuple([player.position for player in players])
        return max(self.wins((0, 0), positions, 0))

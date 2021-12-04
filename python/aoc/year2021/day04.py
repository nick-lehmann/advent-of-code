# Link: https://adventofcode.com/2021/day/4
from typing import List, Tuple
from ..utils import AOCTestCase
from dataclasses import dataclass

@dataclass
class Point:
    num: int
    checked: bool

@dataclass
class Board:
    board: List[List[Point]]
    last_number: int = 0

    def check_number(self, number):
        self.last_number = number
        for row in self.board:
            for el in row:
                if el.num == number:
                    el.checked = True
    
    def is_done(self) -> bool:
        return (
            any(all(el.checked for el in row) for row in self.board) or
            any(all(el.checked for el in column) for column in zip(*self.board))
        )
        
    def __str__(self):
        for row in self.board:
            print(' '.join(str(el.num).ljust(2) for el in row))
    
    def score(self) -> int:
        return sum(sum(el.num for el in row if not el.checked) for row in self.board) * self.last_number

class GiantSquid(AOCTestCase):
    day = 4
    year = 2021

    def read(self, content) -> Tuple[List[int], List[Board]]:
        parts = content.split('\n\n')
        
        drawn = [int(x) for x in parts[0].split(',')]
        boards = [] 
        
        for part in parts[1:]:
            board = []
            lines = part.split('\n')
            for line in lines:
                new = [Point(num=int(c), checked=False) for c in line.split()]
                if len(new):
                    board += [new]
            boards += [Board(board)]
            
        return drawn, boards
    
    def play(self, content):
        drawn, boards = self.read(content) 
        winners = []
        for i, number in enumerate(drawn):
            for i in range(len(boards) - 1, -1, -1):
                board = boards[i]
                board.check_number(number)
                if board.is_done():
                    winners.append(board)
                    boards.pop(i)
        return winners 

    def part1(self, content: str) -> int:
        winner = self.play(content)[0]
        return winner.score()

    def part2(self, content: str) -> int:
        winner = self.play(content)[-1]
        return winner.score()

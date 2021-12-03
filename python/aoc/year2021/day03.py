# Link: https://adventofcode.com/2021/day/3
from ..utils import AOCTestCase


class BinaryDiagnostic(AOCTestCase):
    day = 3
    year = 2021

    def part1(self, content: str) -> int:
        lines = self.lines(content)
        width = len(lines[0])

        ones = [0] * width
        zeros = [0] * width
        
        for line in lines:
            for i in reversed(range(width)):
                c = line[i]
                if c == '0':
                    zeros[i] += 1
                if c == '1':
                    ones[i] += 1
        
        epsilon, gamma = 0, 0
        for i in reversed(range(width)):
            if ones[i] > zeros[i]:
                gamma += 2 ** (width - i - 1)
            if zeros[i] > ones[i]:
                epsilon += 2 ** (width - i - 1)
        
        return epsilon * gamma
            

    def part2(self, content: str) -> int:
        lines = self.lines(content)
        width = len(lines[0])

        def count_most_common(candidates):
            ones = [0] * width
            zeros = [0] * width
            
            for line in candidates:
                for i in range(width):
                    c = line[i]
                    if c == '0':
                        zeros[i] += 1
                    if c == '1':
                        ones[i] += 1
            
            return ['1' if ones[i] >= zeros[i] else '0' for i in range(width)]
        
        def find_rating(op): 
            candidates = lines[:]

            for i in range(width):
                most_common = count_most_common(candidates)
                candidates = [c for c in candidates if op(c[i],most_common[i])]
                
                if len(candidates) == 1:
                    return int(candidates[0], 2)
        
        return find_rating(lambda x,y: x == y) * find_rating(lambda x,y: x != y)

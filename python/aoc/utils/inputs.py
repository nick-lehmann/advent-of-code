from typing import List, Set

"""
Provides a variety of functions for reading input files. 
"""
class InputMixin:
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

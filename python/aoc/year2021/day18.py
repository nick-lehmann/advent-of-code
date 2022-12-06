# Link: https://adventofcode.com/2021/day/18
from typing import List, Union
from ..utils import AOCTestCase
import ast
from dataclasses import dataclass


@dataclass
class Node:
    left: Union['Node', int] = 0
    right: Union['Node', int] = 0
    level: int = 0
    parent: 'Node' = None
    
    def find_children(self) -> List['Node']:
        if all(isinstance(x, int) for x in [self.left, self.right]):
            return [self]

        children = []
        for child in [self.left, self.right]:
            if isinstance(child, Node):
                children += child.find_children()
        return children


class Snailfish(AOCTestCase):
    day = 18
    year = 2021

    def parse(self, line: str) -> Node:
        """
        Parse expressions like [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]] into nodes
        [4,5]
        """
        ast_tree = ast.parse(line)
        l = ast_tree.body[0].value
        
        return self.parse_ast_list(l)
    
    def parse_ast_list(self, ast_node: Union[ast.List, ast.Constant], level=1) -> Node:
        node = Node(level=level) 

        ast_left, ast_right = ast_node.elts 
        
        if isinstance(ast_left, ast.List):
            node.left = self.parse_ast_list(ast_left, level=level+1)
            node.left.parent = node
        else:
            node.left = ast_left.value 
        
        if isinstance(ast_right, ast.List):
            node.right = self.parse_ast_list(ast_right, level=level+1)
            node.right.parent = node
        else:
            node.right = ast_right.value 

        return node

    def part1(self, content: str) -> int:
        line = self.lines(content)[0]
        root = self.parse(line)

        for child in root.find_children():
            print(f"[{child.left},{child.right}] ({child.level})")
        return 10

    def part2(self, content: str) -> int:
        pass

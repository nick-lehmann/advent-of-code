# Link: https://adventofcode.com/2022/day/7
from ..utils import AOCTestCase
from typing import Optional, Union
from dataclasses import dataclass


@dataclass
class Node:
    name: str
    children: list[Union["Node", int]]
    parent: Optional["Node"]


class NoSpaceLeftOnDevice(AOCTestCase):
    day = 7
    year = 2022

    part1 = 0

    def get_tree(self, content: str) -> Node:
        lines = self.lines(content)

        node = Node(name="", parent=None, children=[])
        root = node

        i = 1  # Skip first line, always `cd /`
        while i <= len(lines):
            line = lines[i]
            print("Current line: ", line)
            line = line[2:]  # Strip `$ `

            if line.startswith("ls"):
                i += 1
                try:
                    while not lines[i].startswith("$"):
                        (first, second) = lines[i].split(" ")
                        if first == "dir":
                            node.children.append(
                                Node(parent=node, name=second, children=[])
                            )
                        else:
                            node.children.append(int(first))
                        i += 1
                        # print(node)
                except IndexError:
                    break

            if line.startswith("cd"):
                line = line[3:]

                if line == "..":
                    node = node.parent
                else:
                    for child in node.children:
                        if isinstance(child, Node) and child.name == line:
                            node = child
                            break
                    else:
                        raise ValueError(f"Could not find child {line}")
                i += 1

        return root

    def size_walker(self, node: Node) -> int:
        size = 0
        for child in node.children:
            if isinstance(child, Node):
                size += self.size_walker(child)
            else:
                size += child

        if size < 100000:
            print(f"{node.name} has a size of {size}")
            self.part1 += size

        return size

    def part1(self, content: str) -> int:
        root = self.get_tree(content)
        size = self.size_walker(root)
        print(size)
        return self.part1

    def part2(self, content: str) -> int:
        pass


input = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

if __name__ == "__main__":
    NoSpaceLeftOnDevice().part1(input)

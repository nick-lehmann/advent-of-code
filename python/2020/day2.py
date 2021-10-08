from typing import List
import re
from operator import xor

# https://regex101.com/r/RTevsV/1/ 
PASSWORD_REGEX = r'(\d+)\-(\d+) (\w)\: (\w+)'

def part1(lines: List[str]) -> int:
  valid = 0
  for line in lines:
    match = re.match(PASSWORD_REGEX, line, re.M|re.I) 
    minimum, maximum, letter, password = match.groups()
    minimum = int(minimum)
    maximum = int(maximum)

    count = password.count(letter) 
    if minimum <= count <= maximum:
      valid += 1
  return valid


def part2(lines: List[str]) -> int:
  valid = 0
  for line in lines:
    match = re.match(PASSWORD_REGEX, line, re.M|re.I) 
    first, second, letter, password = match.groups()
    if xor(password[int(first) - 1] == letter, password[int(second) - 1] == letter):
      valid += 1
  return valid
    
    
if __name__ == '__main__':
    with open("../../exercises/2020/02.txt") as file:
        lines = file.readlines()
        print(part1(lines))
        print(part2(lines))

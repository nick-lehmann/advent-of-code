from typing import List


def part1(raw: List[str]) -> int:
    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    valid = 0
    for lines in raw.split('\n\n'):
      parts = {part.split(':')[0] for part in lines.replace('\n', ' ').split(' ')}
      valid += int(not (required_fields - parts))
    return valid


if __name__ == '__main__':
    with open("../../exercises/2020/04.txt") as file:
        raw = file.read()
        print(part1(raw))
        # print(part2(raw))
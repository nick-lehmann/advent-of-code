from utils import AOCTestCase


class PassportProcessing(AOCTestCase):
    def part1(self) -> int:
        required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
        valid = 0
        for lines in self.lines.join("\n").split("\n\n"):
            parts = {part.split(":")[0] for part in lines.replace("\n", " ").split(" ")}
            valid += int(not (required_fields - parts))
        return valid

    def part2(self) -> int:
        pass

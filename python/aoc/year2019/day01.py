from ..utils import AOCTestCase


def fuel_for_mass(mass: int) -> int:
    return max(mass // 3 - 2, 0)


def fuel_for_mass2(mass: int) -> int:
    total = new_fuel = fuel_for_mass(mass)
    while (new_fuel := fuel_for_mass(new_fuel)) > 0:
        total += new_fuel
    return total


class TheTyrannyOfTheRocketEquation(AOCTestCase):
    day = 1
    year = 2019

    def part1(self, content: str) -> int:
        numbers = self.ints(content)
        return sum(fuel_for_mass(mass) for mass in numbers)

    def part2(self, content: str) -> int:
        numbers = self.ints(content)
        return sum(fuel_for_mass2(mass) for mass in numbers)

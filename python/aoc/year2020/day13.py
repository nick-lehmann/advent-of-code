# Link: https://adventofcode.com/2020/day/13
from ..utils import AOCTestCase
from functools import reduce
import math


def euclidean_greatest_common_denominator(a, b):
    if not b:
        return 1, 0, a
    q, r = a // b, a % b
    s, t, g = euclidean_greatest_common_denominator(b, r)
    return t, s - q * t, g


def chinese_remainder_theorem(
    remainder1: int, modulus1: int, remainder2: int, modulus2: int
) -> tuple[int, int]:
    """Only works for coprime moduli."""
    q3 = modulus1 * modulus2
    t, _, g = euclidean_greatest_common_denominator(modulus1 + modulus2, q3)
    r3 = (remainder1 * modulus2 + remainder2 * modulus1) * t
    assert not r3 % g
    r3 = r3 // g % q3
    if (r3 < 0) != (q3 < 0):
        r3 += q3
    return r3, q3


class ShuttleSearch(AOCTestCase):
    day = 13
    year = 2020

    def part1(self, content: str) -> int:
        lines = self.lines(content)
        timestamp = int(lines[0])
        buses = [int(bus) for bus in lines[1].split(",") if bus != "x"]

        next_bus = None
        next_time = 1000000000000

        for bus in buses:
            arrvies_at = (timestamp // bus + 1) * bus - timestamp
            if arrvies_at < next_time:
                next_time = arrvies_at
                next_bus = bus

        return next_bus * next_time

    def part2(self, content: str) -> int:
        lines = self.lines(content)
        buses = lines[1].split(",")

        q, r = 0, 1
        for offset, bus in enumerate(buses):
            if bus == "x":
                continue
            bus = int(bus)
            q, r = chinese_remainder_theorem(q, r, (-offset) % bus, bus)
        return q

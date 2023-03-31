# Link: https://adventofcode.com/2022/day/16
from collections import defaultdict
from ..utils import AOCTestCase
from dataclasses import dataclass
import re

PATTERN = re.compile(
    r"Valve (\w+) has flow rate=(\d+); "
    r"(?:tunnel leads to valve|tunnels lead to valves) (\w+(?:, \w+)*)"
)

RoomName = str


@dataclass
class Room:
    name: RoomName
    flow: int
    neighbors: list[str]


@dataclass
class Link:
    room: str
    opened_at: int

    def __str__(self):
        return f"Open {self.room} at {self.opened_at}"


Rooms = dict[RoomName, "Room"]


class ProboscideaVolcanium(AOCTestCase):
    day = 16
    year = 2022

    Distances = dict[tuple[RoomName, RoomName], int]
    distances: Distances
    rooms: Rooms

    def read(self, content: str) -> Rooms:
        return {
            (match := re.match(PATTERN, line)).group(1): Room(
                name=match.group(1),
                flow=int(match.group(2)),
                neighbors=match.group(3).split(", "),
            )
            for line in self.lines(content)
        }

    def calc_distances(self, rooms: Rooms) -> Distances:
        distances = defaultdict(lambda: float("inf"))
        names = list(rooms.keys())
        for start in names:
            distances[(start, start)] = 0
            for other in rooms[start].neighbors:
                distances[(start, other)] = 1
                distances[(other, other)] = 0  # TODO: Needed?
        for start in names:
            for end in names:
                for middle in names:
                    distances[(start, end)] = min(
                        distances[(start, end)],
                        distances[(start, middle)] + distances[(middle, end)],
                    )
        return distances

    def dfs(
        self, current: RoomName, remaining: set[RoomName], time: int
    ) -> tuple[int, list[Link]]:
        if time == 0:
            return 0, []

        here = self.rooms[current].flow * time
        best, best_chain = 0, []
        for room in remaining:
            if self.distances[(current, room)] >= time:
                continue

            opens_at = time - self.distances[(current, room)] - 1
            released, chain = self.dfs(room, remaining - {room}, opens_at)
            if released > best:
                best, best_chain = released, [Link(room, opens_at)] + chain

        return here + best, best_chain

    def part1(self, content: str) -> int:
        self.rooms = self.read(content)
        self.distances = self.calc_distances(self.rooms)
        release, chain = self.dfs(
            "AA", {room.name for room in self.rooms.values() if room.flow > 0}, 30
        )

        # Open IP at 27
        # Open OD at 23
        # Open ZJ at 20
        # Open UF at 16
        # Open CW at 12
        # Open SB at 9
        # Open PD at 5
        # Open CL at 1

        for link in chain:
            print(f"Open {link.room} at {30 - link.opened_at}")

        # self.graphviz()

        return release

    def part2(self, content: str) -> int:
        pass

    def graphviz(self) -> str:
        def vertix(room: RoomName) -> str:
            return f"{room}{self.rooms[room].flow}"

        for name, room in self.rooms.items():
            for neighbor in room.neighbors:
                print(f"{vertix(name)} -- {vertix(neighbor)}")

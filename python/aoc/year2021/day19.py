#!/usr/bin/python3
import itertools
from collections import defaultdict
from typing import List, Tuple, Dict

data = open("../../../exercises/2021/19.in").read().strip()

TOTAL_ORIENTATIONS = 48

Orientation = int
Point = Tuple[int, int, int]
Beacons = List[Point]
Scanner = List[Beacons]


def read(content: str) -> List[Scanner]:
    scannersRaw = content.split("\n\n")
    scanners = []
    for scanner in scannersRaw:
        beacons: Beacons = []
        for line in scanner.split("\n"):
            line = line.strip()
            if line.startswith("--"):
                continue
            x, y, z = [int(v) for v in line.split(",")]
            beacons.append((x, y, z))
        scanners.append(beacons)
    return scanners


permutations = list(itertools.permutations([0, 1, 2]))


def adjust(point: Point, d: Orientation) -> Point:
    new_point = [point[0], point[1], point[2]]
    for i, p in enumerate(permutations):
        if d // 8 == i:
            new_point = [new_point[p[0]], new_point[p[1]], new_point[p[2]]]

    if d % 2 == 1:
        new_point[0] *= -1
    if (d // 2) % 2 == 1:
        new_point[1] *= -1
    if (d // 4) % 2 == 1:
        new_point[2] *= -1
    return new_point


scanners = read(data)

number_of_scanners = len(scanners)
final_scanners = set(scanners[0])
positions = [None for _ in range(number_of_scanners)]
positions[0] = (0, 0, 0)

good_scanners = set([0])
bad_scanners = set([x for x in range(1, number_of_scanners)])

adjustments = {}
for scannerIndex, scanner in enumerate(scanners):
    for orientation in range(TOTAL_ORIENTATIONS):
        adjustments[(scannerIndex, orientation)] = [adjust(p, orientation) for p in scanner]

while bad_scanners:
    found = None
    for bad_scanner in bad_scanners:
        if found:
            continue

        g = 0
        good_scan = [
            tuple(
                [
                    scanner[0] + positions[g][0],
                    scanner[1] + positions[g][1],
                    scanner[2] + positions[g][2],
                ]
            )
            for scanner in final_scanners
        ]
        for new_orientation in range(TOTAL_ORIENTATIONS):
            bad_scan = adjustments[(bad_scanner, new_orientation)]
            VOTE: Dict[Point, int] = defaultdict(int)

            for bi in range(len(scanners[bad_scanner])):
                for gi in range(len(good_scan)):
                    dp = tuple(
                        [-x1 + x2 for x1, x2 in zip(bad_scan[bi], good_scan[gi])]
                    )
                    VOTE[dp] += 1

            for (dx, dy, dz), val in VOTE.items():
                if val >= 12:
                    positions[bad_scanner] = (dx, dy, dz)
                    # print(f'FOUND {b} via {g} at (x={dx} y={dy} z={dz})')
                    for p in bad_scan:
                        final_scanners.add(tuple([p[0] + dx, p[1] + dy, p[2] + dz]))
                    found = bad_scanner

    print(bad_scanners, found)
    bad_scanners.remove(found)
    good_scanners.add(found)

print(len(final_scanners))

max_distance = 0
for p1 in positions:
    for p2 in positions:
        distance = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])
        max_distance = max(max_distance, distance)
print(max_distance)

# Link: https://adventofcode.com/2021/day/16
from ..utils import AOCTestCase
from typing import Any, List, Optional
from dataclasses import dataclass


@dataclass
class Packet:
    version: int
    type: int
    subpackets: List["Packet"]
    literal: Optional[int] = None
    size: Optional[int] = None


class PacketDecoder(AOCTestCase):
    day = 16
    year = 2021

    def read(self, content):
        line = self.lines(content)[0]
        binary_line = "".join(format(int(x, 16), "04b") for x in line)
        packet = parser(binary_line)

        return packet

    def part1(self, content: str) -> int:
        return get_sum_of_versions(self.read(content))

    def part2(self, content: str) -> int:
        return operate(self.read(content))


def parser(line: str) -> Packet:
    print(f"Parsing {line}")
    version = int(line[0:3], 2)
    type = int(line[3:6], 2)

    if type == 4:
        # Literal
        whole_number: str = ""
        i = 0
        while True:
            additional_bits = line[(i * 5) + 6 : (i * 5) + 11]
            whole_number += additional_bits[1:]
            if additional_bits[0] == "0":
                break
            i += 1
        return Packet(
            version=version,
            type=type,
            literal=int(whole_number, 2),
            size=len(whole_number),
            subpackets=[],
        )
    else:
        # Operator
        length_type = int(line[6])
        if length_type == 0:
            # Length Type Operator
            total_length_of_subpackets = int(line[7:22], 2)
            subpackets = []
            start_of_data = 22
            while sum(s.size for s in subpackets) < total_length_of_subpackets:
                subpackets += [parser(line[start_of_data:])]
                start_of_data += subpackets[-1].size
        else:
            # Subpacket Count Type Operator
            num_subpackets = int(line[7:18], 2)
            subpackets = []
            start_of_data = 18
            while len(subpackets) < num_subpackets:
                subpackets += [parser(line[start_of_data:])]
                start_of_data += subpackets[-1].size
        return Packet(
            version=version, type=type, size=start_of_data, subpackets=subpackets
        )


def operate(packet: Packet):
    packet_type = packet.type
    if packet_type == 0:
        # Sum
        return sum(operate(p) for p in packet.subpackets)
    elif packet_type == 1:
        # Product
        i = 1
        for p in packet.subpackets:
            i *= operate(p)
        return i
    elif packet_type == 2:
        # Minimum
        return min(operate(p) for p in packet.subpackets)
    elif packet_type == 3:
        # Maximum
        return max(operate(p) for p in packet.subpackets)
    elif packet_type == 4:
        # Literal
        return packet.literal
    elif packet_type == 5:
        # Greater than
        return 1 if operate(packet.subpackets[0]) > operate(packet.subpackets[1]) else 0
    elif packet_type == 6:
        # Less than
        return 1 if operate(packet.subpackets[0]) < operate(packet.subpackets[1]) else 0
    elif packet_type == 7:
        # Equal to
        return (
            1 if operate(packet.subpackets[0]) == operate(packet.subpackets[1]) else 0
        )


def get_sum_of_versions(packet: Packet) -> int:
    return sum(get_sum_of_versions(p) for p in packet.subpackets) + packet.version

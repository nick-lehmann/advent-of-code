---
to: rust/src/aoc<%= year %>/day<%= dayPadded %>.rs
unless_exists: true
---
/// Name: <%= name %>
/// URL: https://adventofcode.com/<%= year %>/day/<%= day %>


use crate::{gym::Groups, prelude::*};

fn part1(line: String) -> Result<u64, Error> {
  todo!()
}

aoc_test!(part1, <%= year %>, <%= day %>, "part1");

fn part2(line: String) -> Result<u64, Error> {
  todo!()
}

aoc_test!(part2, <%= year %>, <%= day %>, "part2");

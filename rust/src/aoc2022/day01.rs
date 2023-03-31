///! Link: https://adventofcode.com/2022/day/1
use crate::{gym::Groups, prelude::*};
use log::debug;
use std::cmp::Reverse;

fn part1(elves: Groups<Vec<i64>>) -> Result<i64, Error> {
    elves
        .iter()
        .map(|elf| elf.iter().sum::<i64>())
        .max()
        .ok_or_else(|| "Unable to find maximun".into())
}
aoc_test!(part1, 2022, 1, "part1");

fn part2(elves: Groups<Vec<i64>>) -> Result<i64, Error> {
    let mut calories: Vec<i64> = elves.iter().map(|elf| elf.iter().sum::<i64>()).collect();
    calories.sort_unstable_by_key(|c| Reverse(*c));

    let top_elves = calories[0..3].to_vec();
    debug!("Top three elves by calories: {:?}", top_elves);

    Ok(top_elves.iter().sum::<i64>() as i64)
}
aoc_test!(part2, 2022, 1, "part2");

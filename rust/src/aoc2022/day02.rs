///! Link: https://adventofcode.com/2020/day/2
use crate::prelude::*;
use std::{cmp::Ordering, convert::TryFrom, str::FromStr};

#[derive(Debug, PartialEq)]
enum Choice {
    Paper,
    Rock,
    Scissors,
}

impl Choice {
    pub fn score(&self) -> u32 {
        match self {
            Choice::Rock => 1,
            Choice::Paper => 2,
            Choice::Scissors => 3,
        }
    }
}

impl PartialOrd for Choice {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(match self {
            Choice::Paper => match other {
                Choice::Paper => Ordering::Equal,
                Choice::Rock => Ordering::Greater,
                Choice::Scissors => Ordering::Less,
            },
            Choice::Rock => match other {
                Choice::Paper => Ordering::Less,
                Choice::Rock => Ordering::Equal,
                Choice::Scissors => Ordering::Greater,
            },
            Choice::Scissors => match other {
                Choice::Paper => Ordering::Greater,
                Choice::Rock => Ordering::Less,
                Choice::Scissors => Ordering::Equal,
            },
        })
    }
}

impl TryFrom<&str> for Choice {
    type Error = Error;

    fn try_from(value: &str) -> Result<Self, Self::Error> {
        match value {
            "A" | "X" => Ok(Choice::Rock),
            "B" | "Y" => Ok(Choice::Paper),
            "C" | "Z" => Ok(Choice::Scissors),
            _ => Err("Invalid choice".into()),
        }
    }
}

#[derive(Debug)]
struct Play {
    pub you: Choice,
    pub they: Choice,
}

// TODO: Maybe a new type for converting form line? Autoimplement `FromStr` for all implementors.
impl FromStr for Play {
    type Err = String;

    fn from_str(line: &str) -> Result<Self, Self::Err> {
        let parts: Vec<&str> = line.split_whitespace().collect();

        Ok(Play {
            they: Choice::try_from(parts[0])?,
            you: Choice::try_from(parts[1])?,
        })
    }
}

fn part1(guide: Vec<Play>) -> Result<i64, Error> {
    let mut score = 0;
    for play in guide {
        match play.you.partial_cmp(&play.they) {
            Some(Ordering::Greater) => score += 6,
            Some(Ordering::Equal) => score += 3,
            Some(Ordering::Less) => score += 0,
            None => return Err("Invalid play".into()),
        }
        score += play.you.score() as i64;
    }

    Ok(score)
}
aoc_test!(part1, 2022, 2, "part1");

fn part2() -> Result<i64, Error> {
    todo!()
}

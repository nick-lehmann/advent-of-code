///! Link: https://adventofcode.com/2020/day/2
use crate::prelude::*;
use log::debug;
use regex::Regex;
use std::{
    convert::{TryFrom, TryInto},
    str::FromStr,
};

#[derive(Debug, PartialEq)]
pub struct Policy {
    pub first: usize,
    pub second: usize,
    pub letter: char,
    pub password: String,
}

impl FromStr for Policy {
    type Err = &'static str;

    fn from_str(value: &str) -> Result<Self, Self::Err> {
        let pattern = Regex::new(r"(\d+)-(\d+) (\w): (\w*)").unwrap();
        let captures = pattern.captures(&value).ok_or("Unable to parse line")?;

        // TODO: Create helper for extracting from regex captures.
        Ok(Policy {
            first: captures
                .get(1)
                .ok_or("Unable to find capture 1")?
                .as_str()
                .parse()
                .map_err(|_| "Unable to convert first")?,
            second: captures
                .get(2)
                .ok_or("Unable to find capture 2")?
                .as_str()
                .parse()
                .map_err(|_| "Unable to convert second")?,
            letter: captures
                .get(3)
                .ok_or("Unable to find capture 3")?
                .as_str()
                .parse()
                .map_err(|_| "Unable to convert letter")?,
            password: captures
                .get(4)
                .ok_or("Unable to find capture 4")?
                .as_str()
                .parse()
                .map_err(|_| "Unable to convert password")?,
        })
    }
}

fn part1(policies: Vec<Policy>) -> Result<i64, Error> {
    Ok(policies
        .iter()
        .map(|policy| {
            let count = policy
                .password
                .chars()
                .filter(|c| c == &policy.letter)
                .count();
            (count >= policy.first && count <= policy.second) as i64
        })
        .sum())
}
aoc_test!(part1, 2020, 2, "part1");

fn is_char_at(s: &str, i: usize, c: char) -> bool {
    match s.chars().nth(i - 1) {
        Some(x) => x == c,
        None => false,
    }
}

/// Check if the letter is at either the first or second position.
///
/// ```
/// use advent_of_code::aoc2020::day02::{Policy, valid_at_position};
///
/// let valid = Policy {
///     first: 1,
///     second: 2,
///     letter: 'a',
///     password: "ab".to_string(),
/// };
/// assert_eq!(valid_at_position(&valid), true);
///
/// ```
pub fn valid_at_position(policy: &Policy) -> bool {
    let result = is_char_at(&policy.password, policy.first, policy.letter)
        ^ is_char_at(&policy.password, policy.second, policy.letter);

    debug!("{:?} => {}", policy, result);
    result
}

fn part2(policies: Vec<Policy>) -> Result<i64, Error> {
    Ok(policies
        .iter()
        .map(|policy| valid_at_position(policy) as i64)
        .sum())
}
aoc_test!(part2, 2020, 2, "part2");

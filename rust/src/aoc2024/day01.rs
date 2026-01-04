use crate::{gym::Groups, prelude::*};
use log::debug;
use std::{collections::HashMap, ops::Add};

fn parse_line(line: &str) -> (u32, u32) {
    let (l, r) = line.split_once(|c: char| c.is_ascii_whitespace()).unwrap();
    let l = l.parse().unwrap();
    let r = r.trim_start().parse().unwrap();
    (l, r)
}

fn part1(lines: Vec<String>) -> Result<u32, Error> {
    let mut left: Vec<u32> = Vec::new();
    let mut right: Vec<u32> = Vec::new();

    for line in lines {
        let (l, r) = parse_line(&line);
        left.push(l);
        right.push(r);
    }

    left.sort();
    right.sort();

    Ok(left
        .iter()
        .zip(right.iter())
        .map(|(l, r)| l.abs_diff(*r))
        .sum())
}

aoc_test!(part1, 2024, 1, "part1");

fn part2(lines: Vec<String>) -> Result<u32, Error> {
    let mut left: Vec<u32> = Vec::new();

    let mut right: HashMap<u32, u32> = HashMap::new();

    for line in lines {
        let (l, r) = parse_line(&line);
        left.push(l);
        *right.entry(r).or_default() += 1;
    }

    println!("L: {:?}", left);
    println!("R: {:?}", right);

    let mut total_diff: u32 = 0;
    for l in left {
        let r = right.get(&l).unwrap_or(&0);
        let similarity = l * r;

        println!("Similarity for {}: {}", l, similarity);
        total_diff += similarity;
    }

    Ok(total_diff)
}

aoc_test!(part2, 2024, 1, "part2");

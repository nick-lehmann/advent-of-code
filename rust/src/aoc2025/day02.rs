use crate::{gym::Groups, prelude::*};
use itertools::Itertools;
use log::debug;
use std::{collections::HashMap, ops::Add};

fn part1(line: String) -> Result<u64, Error> {
    let mut total = 0;

    for range in line.strip_suffix('\n').unwrap().split(',') {
        let (start_raw, end_raw) = range.split_once('-').expect("Range is invalid");
        let start: u64 = start_raw
            .parse()
            .expect(&format!("Invalid start {start_raw} in {range}"));
        let end: u64 = end_raw
            .parse()
            .expect(&format!("Invalid end {end_raw} in {range}"));

        for i in (start..end + 1) {
            let num = i.to_string();

            // Numbers with an odd amount of digit do not count (I think)
            if num.len() % 2 != 0 {
                continue;
            }

            let mut s = num.to_string();
            let end = s.split_off(s.len() / 2);

            if s == end {
                total += i
            }
        }
    }

    Ok(total)
}

aoc_test!(part1, 2025, 2, "part1");

fn part2(line: String) -> Result<u64, Error> {
    let mut total = 0;

    for range in line.strip_suffix('\n').unwrap().split(',') {
        let (start_raw, end_raw) = range.split_once('-').expect("Range is invalid");
        let start: u64 = start_raw
            .parse()
            .expect(&format!("Invalid start {start_raw} in {range}"));
        let end: u64 = end_raw
            .parse()
            .expect(&format!("Invalid end {end_raw} in {range}"));

        println!("Start: {start}, End: {end}");
        for i in (start..end + 1) {
            let num = i.to_string();

            for l in (1..(num.len() / 2) + 1) {
                // println!("Checking length: {l}");
                if num.len() % l != 0 {
                    continue;
                }

                let chunk = unsafe { num.slice_unchecked(0, l) };
                let mut is_okay = true;
                for i in (1..num.len() / l) {
                    let chunk2 = unsafe { num.slice_unchecked(i * l, (i + 1) * l) };

                    if (chunk != chunk2) {
                        is_okay = false;
                        break;
                    }
                }

                if (is_okay) {
                    println!("{num} is a dummy");
                    total += i;
                    break;
                }
            }
        }
    }

    Ok(total)
}

aoc_test!(part2, 2025, 2, "part2");

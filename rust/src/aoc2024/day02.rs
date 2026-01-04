use crate::{gym::Groups, prelude::*};
use log::debug;

fn check_values(values: &[i32]) -> bool {
    let mut direction = 0;

    for win in values.windows(2) {
        let diff = win[0] - win[1];

        if (diff.abs() > 3 || diff == 0) {
            return false;
        }

        if (diff > 0 && direction >= 0) {
            direction = 1;
            continue;
        }
        if (diff < 0 && direction <= 0) {
            direction = -1;
            continue;
        }

        return false;
    }

    true
}

fn part1(lines: Vec<String>) -> Result<u32, Error> {
    let mut total: u32 = 0;

    for line in lines {
        let nums: Vec<i32> = line
            .split_ascii_whitespace()
            .map(|num| num.parse().unwrap())
            .collect();

        debug!("Nums: {:?}", nums);

        if (check_values(&nums)) {
            total += 1;
            debug!("Safe")
        } else {
            debug!("Unsafe")
        }
    }

    Ok(total)
}

aoc_test!(part1, 2024, 2, "part1");

fn part2(lines: Vec<String>) -> Result<u32, Error> {
    let mut total: u32 = 0;

    for line in lines {
        let nums: Vec<i32> = line
            .split_ascii_whitespace()
            .map(|num| num.parse().unwrap())
            .collect();

        debug!("Nums: {:?}", nums);

        let is_safe = check_values(&nums)
            || (0..nums.len()).any(|i| {
                let mut copy = nums.clone();
                copy.remove(i);
                check_values(&copy)
            });

        if (is_safe) {
            total += 1;
            debug!("Safe")
        } else {
            debug!("Unsafe")
        }
    }

    Ok(total)
}
aoc_test!(part2, 2024, 2, "part2");

///! Link: https://adventofcode.com/2020/day/1
use crate::prelude::*;
use std::cmp::Ordering;

static TARGET: i32 = 2020;

/// Naive solution.
///
/// For each number in the list, check if 2020 subtracted the number is in the list.
/// Complexity: O(n^2)
pub fn part1_naive(nums: Vec<i32>) -> Result<i64, Error> {
    for number in &nums {
        let remainder = 2020 - number;
        if nums.contains(&remainder) {
            return Ok((remainder * number).into());
        }
    }

    Err("No solution found".into())
}
aoc_test!(part1_naive, 2020, 1, "part1");

/// Sorts list, takes numbers from the left and compares it to number taken from the right.
///
/// Complexity: O(n^2)?
pub fn part1_sorted(mut nums: Vec<i32>) -> Result<i64, Error> {
    nums.sort_unstable();

    for (left, cur) in nums.iter().enumerate() {
        for right in (left + 1..nums.len()).rev() {
            let sum = cur + nums[right];

            match sum.cmp(&TARGET) {
                Ordering::Equal => return Ok((cur * nums[right]) as i64),
                Ordering::Less => break,
                Ordering::Greater => continue,
            };
        }
    }

    Err("No solution found".into())
}
aoc_test!(part1_sorted, 2020, 1, "part1");

/// Takes numbers from the left and searches the right side for the remainder using binary search.
///
/// Complexity: O(n^2)
pub fn part1_binary_search(mut nums: Vec<i32>) -> Result<i64, Error> {
    nums.sort_unstable();

    for (left, cur) in nums.iter().enumerate() {
        let remainder = TARGET - cur;

        match nums[left + 1..].binary_search(&remainder) {
            Ok(right) => return Ok((cur * nums[left + 1 + right]) as i64),
            Err(_) => continue,
        };
    }

    Err("No solution found".into())
}
aoc_test!(part1_binary_search, 2020, 1, "part1");

pub fn part2_naive(nums: Vec<i32>) -> Result<i64, Error> {
    for x in &nums {
        for y in &nums {
            for z in &nums {
                if x + y + z == 2020 {
                    return Ok((x * y * z).into());
                }
            }
        }
    }

    Err("No solution found".into())
}
aoc_test!(part2_naive, 2020, 1, "part2");

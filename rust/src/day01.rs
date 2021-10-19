/// Link: https://adventofcode.com/2020/day/1
pub fn part1(lines: Vec<String>) -> i64 {
    let nums: Vec<i32> = lines
        .into_iter()
        .map(|x| x.parse::<i32>().unwrap())
        .collect();

    for number in &nums {
        let remainder = 2020 - number;
        if nums.contains(&remainder) {
            return (remainder * number).into();
        }
    }
    0
}

pub fn part2(lines: Vec<String>) -> i64 {
    let nums: Vec<i32> = lines
        .into_iter()
        .map(|x| x.parse::<i32>().unwrap())
        .collect();

    for x in &nums {
        for y in &nums {
            for z in &nums {
                if x + y + z == 2020 {
                    return (x * y * z).into();
                }
            }
        }
    }

    0
}

#[cfg(test)]
pub mod tests {
    use super::{part1, part2};
    use crate::util::{run_aoc, AOCFile};

    static YEAR: u32 = 1;
    static DAY: u32 = 1;

    #[test]
    fn test_part1_example() {
        run_aoc(
            part1,
            AOCFile::Example,
            AOCFile::ExampleSolution1,
            YEAR,
            DAY,
        )
    }

    #[test]
    fn test_part1() {
        run_aoc(part1, AOCFile::Puzzle, AOCFile::PuzzleSolution1, YEAR, DAY)
    }

    #[test]
    fn test_part2_example() {
        run_aoc(
            part2,
            AOCFile::Example,
            AOCFile::ExampleSolution2,
            YEAR,
            DAY,
        )
    }

    #[test]
    fn test_part2() {
        run_aoc(part2, AOCFile::Puzzle, AOCFile::PuzzleSolution2, YEAR, DAY)
    }
}

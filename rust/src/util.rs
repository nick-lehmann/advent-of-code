use std::fs::File;
use std::io::{BufRead, BufReader};
use std::path::PathBuf;

// Test a single AOC testcase
pub fn run_aoc(
    func: fn(Vec<String>) -> i64,
    input_type: AOCFile,
    solution_type: AOCFile,
    year: u32,
    day: u32,
) {
    // Find input
    let input_path = get_aoc_path(input_type, year, day);
    let input_file = File::open(&input_path).unwrap();
    let input = read_lines(input_file);
    let input_len = input.len();
    let result: i64 = func(input).into();

    println!("Read {} input lines", input_len);

    // Find solution
    let solution_path = get_aoc_path(solution_type, year, day);
    let solution_file = File::open(&solution_path).unwrap();
    let solution = read_single_integer(solution_file);

    assert_eq!(
        solution, result,
        "Result {} is not equal to solution {}\n",
        result, solution
    );
}

pub enum AOCFile {
    Puzzle,
    PuzzleSolution1,
    PuzzleSolution2,
    Example,
    ExampleSolution1,
    ExampleSolution2,
}

pub fn get_aoc_path(file: AOCFile, year: u32, day: u32) -> PathBuf {
    PathBuf::from(format!(
        "../exercises/{}/{:0>2}/{}",
        year,
        day,
        match file {
            AOCFile::Example => "example.txt",
            AOCFile::ExampleSolution1 => "example_solution1.txt",
            AOCFile::ExampleSolution2 => "example_solution2.txt",
            AOCFile::Puzzle => "puzzle.txt",
            AOCFile::PuzzleSolution1 => "puzzle_solution1.txt",
            AOCFile::PuzzleSolution2 => "puzzle_solution2.txt",
        }
    ))
}

pub fn read_lines(file: File) -> Vec<String> {
    BufReader::new(file)
        .lines()
        .collect::<Result<Vec<String>, _>>()
        .unwrap()
}

pub fn read_single_integer(file: File) -> i64 {
    let mut line: String = "".to_string();
    BufReader::new(file).read_line(&mut line).unwrap();
    println!("Read solution {}", line);
    line.strip_suffix("\n").unwrap().parse().unwrap()
}

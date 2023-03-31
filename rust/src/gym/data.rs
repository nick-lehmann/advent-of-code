use std::collections::HashMap;
use std::env;
use std::path::PathBuf;

use serde::Deserialize;

#[derive(Debug, Deserialize)]
struct AdventOfCodeDay {
    pub tests: HashMap<String, Vec<AdventOfCodeTest>>,
}

#[derive(Debug, Deserialize, Clone)]
pub struct AdventOfCodeTest {
    pub input: String,
    pub solution: String,
}

/// Fetches the task data from the `exercises` directory.
fn get_data(year: u32, day: u32) -> AdventOfCodeDay {
    let path = get_aoc_path(year, day);

    let input = std::fs::read_to_string(path).expect("Unable to read file");
    serde_yaml::from_str(&input).unwrap()
}

pub fn get_testcases(name: &str, year: u32, day: u32) -> Vec<AdventOfCodeTest> {
    let data = get_data(year, day);

    data.tests.get(name).unwrap().to_vec()
}

/// Returns the path to an AoC data file in yaml.
fn get_aoc_path(year: u32, day: u32) -> PathBuf {
    let path = PathBuf::from(format!("../exercises/{}/{:0>2}.yaml", year, day));

    println!(
        "{} {} {}",
        path.display(),
        year,
        env::current_dir().unwrap().display()
    );
    path.canonicalize()
        .expect(&format!("Failed to canonicalize path: {}", path.display()))
}


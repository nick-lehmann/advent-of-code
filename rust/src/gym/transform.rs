///! Transformer convert the plain data for a problem into some kind of datastructure.
///!
///! All data is given as a plain string but problems often start e.g. with an array of integers.
///! Conversions like this are very common. Hence, they are implemented here to not bloat the
///! individual problem implementations.
use std::{convert::TryFrom, str::FromStr};

use grid::Grid;

pub trait FromInput: Sized {
    fn from_input(input: &str) -> Result<Self, String>;
}

impl<Target> FromInput for Vec<Target>
where
    Target: FromStr,
    <Target as FromStr>::Err: std::fmt::Debug,
{
    fn from_input(input: &str) -> Result<Self, String> {
        Ok(input.lines().map(|line| line.parse().unwrap()).collect())
    }
}

impl<Target> FromInput for Grid<Target>
where
    Target: TryFrom<char> + Default,
    <Target as TryFrom<char>>::Error: std::fmt::Debug + 'static,
{
    fn from_input(input: &str) -> Result<Self, String> {
        let lines: Vec<&str> = input.lines().collect();
        let number_of_rows = lines.len();
        let number_of_columns = lines[0].len();

        let mut grid: Grid<Target> = Grid::new(number_of_rows, number_of_columns);

        for (row, line) in lines.iter().enumerate() {
            for (column, character) in line.chars().enumerate() {
                grid[row][column] = Target::try_from(character).unwrap();
            }
        }

        Ok(grid)
    }
}

impl FromInput for String {
    fn from_input(input: &str) -> Result<Self, String> {
        Ok(input.to_string())
    }
}

#[derive(Debug, PartialEq)]
pub struct Groups<T>(Vec<T>);

impl<Target> FromInput for Groups<Target>
where
    Target: FromInput,
{
    fn from_input(input: &str) -> Result<Self, String> {
        let mut inner: Vec<Target> = vec![];

        for group in input.split("\n\n") {
            inner.push(Target::from_input(group)?);
        }

        Ok(Groups(inner))
    }
}

impl<T> std::ops::Deref for Groups<T> {
    type Target = Vec<T>;

    fn deref(&self) -> &Self::Target {
        &self.0
    }
}

///! Link: https://adventofcode.com/2020/day/3
use crate::prelude::*;
use grid::Grid;
use log::debug;
use std::convert::TryFrom;

static SLOPES: &[(usize, usize)] = &[(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)];

#[derive(Default, Debug, PartialEq)]
#[repr(i8)]
pub enum Tile {
    #[default]
    Empty,
    Tree,
}

impl TryFrom<char> for Tile {
    type Error = &'static str;

    fn try_from(value: char) -> Result<Self, Self::Error> {
        match value {
            '#' => Ok(Tile::Tree),
            '.' => Ok(Tile::Empty),
            _ => Err("Invalid tile"),
        }
    }
}

/// For the slope 3 right, 1 down, count all the trees.
pub fn part1(grid: Grid<Tile>) -> Result<i64, Error> {
    let mut col = 0;
    let mut tree_count = 0;
    for row in 0..grid.rows() {
        let cell = grid.get(row, col).ok_or("Invalid grid")?;
        if cell == &Tile::Tree {
            tree_count += 1;
        }
        col = (col + 3) % grid.cols();
    }
    Ok(tree_count)
}
aoc_test!(part1, 2020, 3, "part1");

/// Count the trees for multiple slopes, and multiply the counts together.
pub fn part2(grid: Grid<Tile>) -> Result<i64, Error> {
    debug!("Grid: {:?}x{:?}", grid.rows(), grid.cols());
    let mut total = 1;

    for (i, (right, down)) in SLOPES.iter().enumerate() {
        let mut col = 0;
        let mut tree_count = 0;
        for row in (0..grid.rows()).step_by(*down) {
            let cell = grid.get(row, col).ok_or("Invalid grid")?;
            if cell == &Tile::Tree {
                tree_count += 1;
            }
            col = (col + right) % grid.cols();
        }

        total *= tree_count;
        debug!("Slope {} right, {} down: {}", right, down, tree_count);
    }

    debug!("Tree counts: {:?}", total);
    Ok(total)
}
aoc_test!(part2, 2020, 3, "part2");

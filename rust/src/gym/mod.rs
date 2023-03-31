mod data;
mod solution;
#[macro_use]
mod test;
mod transform;

pub use data::get_testcases;
pub use solution::{Error, Solution};
pub(crate) use test::aoc_test;
pub use transform::{FromInput, Groups};

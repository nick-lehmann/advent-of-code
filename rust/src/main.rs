use std::io::{self, Read};

fn main() {
    let mut stdin = io::stdin().lock();
    let mut input = String::new();
    stdin.read_to_string(&mut input).unwrap();

    println!("{}", input);
}

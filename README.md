Advent of Code
==============

Solutions in different languages:
- Python 
- Typescript
- Kotlin
- Go
- Rust

Problems are usually tackled in this order.

Features
- 1 Easily access resource files
- 2 Parse resources into multiple formats (number, lines, etc.)
- 3 Test command for examples
- 4 Test command for "production"
- 5 Run single tests or all
- 6 Benchmark command
- 7 Generate boilerplate for problems
- 8 Common utils per language in a separate file


| Language   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| Python     | x   | x   | x   | x   | x   |     | x   | x   |
| Typescript |     |     |     |     |     |     |     |     |
| Kotlin     |     |     |     |     |     |     |     |     |
| Go         |     |     |     |     |     |     |     |     |
| Rust       |     |     |     |     |     |     |     |     |


## Generate new days

This project uses [hygen](https://github.com/jondot/hygen) to create new days.

```
> brew install hygen
```

Generate a new day

```
> hygen python day
✔ What's the year? · 2020
✔ What's the day? · 9
✔ What's the name of the day? · Something

Loaded templates: _templates
       added: exercises/2020/09/example_solution.txt
       added: exercises/2020/09/example.txt
       added: exercises/2020/09/puzzle_solution1.txt
       added: exercises/2020/09/puzzle_solution2.txt
       added: exercises/2020/09/puzzle.txt
       added: python/2020/day9.py
```


TODO:
- Helpers for different kinds of maps (e.g. AOC Day 11)

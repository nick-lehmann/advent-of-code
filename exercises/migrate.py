import os
from shutil import rmtree


def migrate(yearPath: str, day: str):
    contents = []
    
    dayPath = os.path.join(yearPath, str(day))
    
    for filename in [
        "example_solution1.txt",
        "example_solution2.txt",
        "example.txt",
        "puzzle_solution1.txt",
        "puzzle_solution2.txt",
        "puzzle.txt",
    ]:
        with open(os.path.join(dayPath, filename)) as f:
            contents += [f.read().strip('\n')]

    (
        example_solution1,
        example_solution2,
        example,
        puzzle_solution1,
        puzzle_solution2,
        puzzle,
    ) = contents

    output = """
inputs:
  example: &example |
{example}
  puzzle: &puzzle |
{puzzle}

tests:
  part1:
    - input: *example
      solution: {example_solution1}
    - input: *puzzle
      solution: {puzzle_solution1} 
  part2:
    - input: *example
      solution: {example_solution2}
    - input: *puzzle
      solution: {puzzle_solution2}
"""

    def indent(lines, n=4):
        return '\n'.join([' ' * n + line for line in lines.split('\n')])

    with open(os.path.join(yearPath, f"{day}.yaml"), "w") as f:
        f.write(output.format(example=indent(example), puzzle=indent(puzzle), 
            example_solution1=example_solution1, puzzle_solution1=puzzle_solution1,
            example_solution2=example_solution2, puzzle_solution2=puzzle_solution2
        ).lstrip('\n'))
    
    rmtree(dayPath)
    

d = "."
yearFolders = [
    os.path.join(d, o) for o in os.listdir(d) if os.path.isdir(os.path.join(d, o))
]

for yearFolder in yearFolders:
    days = [d for d in os.listdir(yearFolder) if os.path.isdir(os.path.join(yearFolder, d))]
    for day in days:
        print(f'Migrating {yearFolder} {day}')
        try:
            migrate(yearFolder, day)
        except Exception as e:
            print('Failed to migrate', e)


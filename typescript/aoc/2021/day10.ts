/**
 * Name: SyntaxScoring
 * URL: https://adventofcode.com/2021/day/10
 */

export const parse = (content: string) => content.split("\n");

const openingBrackets: Record<string, string> = {
  ")": "(",
  "}": "{",
  "]": "[",
  ">": "<",
};

const scores: Record<string, number> = {
  ")": 3,
  "]": 57,
  "}": 1197,
  ">": 25137,
};

const autocomplete_scores = {
  "(": 1,
  "[": 2,
  "{": 3,
  "<": 4,
};

export function part1(lines: string[]): number {
  let score = 0;
  for (const line of lines) {
    const stack: String[] = [];
    for (const char of line) {
      if (char in openingBrackets) {
        if (stack[-1] == openingBrackets[char]) {
          stack.pop();
        } else {
          score += scores[char];
          break;
        }
      } else if (Object.values(openingBrackets).includes(char)) {
        stack.push(char);
      }
    }
  }

  return score;
}

export function part2(lines: string[]): number {
  const scores = [];
  for (const line of lines) {
    const stack: string[] = []
    for (const char of line) {
      if (Object.keys(openingBrackets).includes(char)) {
        if (stack[-1] == openingBrackets[char]) {
          stack.pop()
        } else {
          break
        }
      } else {
        stack.push(char)
      }
    }  
  }

}

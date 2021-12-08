/**
 * Name: SevenSegmentSearch
 * URL: https://adventofcode.com/2021/day/8
 */
 
const sortLetters = (letters: string) => Array.from(letters).sort().join('')

type Clock = {
  signal: string[]
  output: string[]
}

export const parse = (content: string) => 
  content
    .trim()
    .split('\n')
    .map((s) => s.split(' | ') as [string, string])
    .map(([signal, output]) => ({
      signal: signal.split(' ').map(sortLetters),
      output: output.split(' ').map(sortLetters),
    }))

export function part1(clocks: Clock[]): number {
  const targetLenghts = [2, 3, 4, 7] 
  const isSearchedNumber = (s: string) => targetLenghts.includes(s.length)

  return clocks
    .map(({ output }) => output.filter(isSearchedNumber).length)
    .reduce((a, b) => a + b, 0)
}

export function part2(ints: number[]): number {
  throw new Error('Not implemented')
}

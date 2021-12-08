/**
 * Name: Sonar Sweep 
 * URL: https://adventofcode.com/2021/day/1
 */

export const parse = (content: string) => content.split('\n').filter(Boolean).map(Number)

export function part1(ints: number[]): number {
    let increase = 0
    for (let i = 0; i < ints.length - 1; i++) {
      if (ints[i] < ints[i + 1]) {
        increase += 1
      }
    }
    return increase
}

export function part2(ints: number[]): number | null {
  let counter = 0
  let prevNumber = Number.POSITIVE_INFINITY
  for (let i = 2; i < ints.length; i++) {
    const number = ints[i] + ints[i - 1] + ints[i - 2]
    if (number > prevNumber) {
      counter++
    }
    prevNumber = number
  }
  return counter
}

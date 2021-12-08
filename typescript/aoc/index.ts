import * as fs from 'fs'
import * as yaml from 'js-yaml'

type AOCDay = {
  parse: (input: string) => any,
  part1: (input: any) => number,
  part2: (input: any) => number,
}
  
type AOCPartInput = {
  input: string,
  solution: number
}

type AOCDayInput = AOCPartInput[]
  
type AOCDayConfig = {
  inputs: {
    [key: string]: string
  },
  tests: {
    part1: AOCDayInput
    part2: AOCDayInput
  }
}

const year = parseInt(process.argv[2], 10)
const day = parseInt(process.argv[3], 10)

if (Number.isNaN(day) || day < 1 || day > 25) {
  console.error('You have to choose a day between 1 and 25')
  console.error('For example: node src/index.js 1')
  process.exit(1)
}

const paddedDay = day.toString().padStart(2, '0')

const inputFile = `../exercises/${year}/${paddedDay}.yaml`
const programFile = `./${year}/day${paddedDay}.ts`

const config = yaml.load(fs.readFileSync(inputFile, 'utf8')) as AOCDayConfig
// console.log(config)

const callback = require(programFile) as AOCDay
// console.log(callback)

for (const [partName, parts] of Object.entries(config.tests)) {
  console.log(`Running ${partName}`) 
  
  for (const part in parts) {
    const { input, solution } = parts[part]
    
    const parsedInput = callback.parse(input)
    
    // @ts-ignore
    const result = callback[partName](parsedInput)
    console.log(`${partName} ${part}: ${result}`)
    if (result !== solution) {
      console.error(`${partName} ${part} failed`)
      process.exit(1)
    }
  }
}

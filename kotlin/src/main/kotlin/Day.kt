import java.io.File

abstract class Day(dayNumber: Int) {
    abstract val title: String
    protected val inputString: String by lazy { getResource(dayNumber).readText() }
    protected val inputLines: List<String> by lazy { getResource(dayNumber).readLines().filter { it != "" } }
    protected val inputInts: List<Int> by lazy { inputLines.map { it.toInt() } }

    abstract fun part1(): Any
    abstract fun part2(): Any

    private fun getResource(day: Int): File {
        val filename = day.toString().padStart(2, '0')
        return File("/Users/nick/Projekte/advent-of-code/exercises/2020/$filename/puzzle.txt")
    }

    public fun run() {
        println("Part1: ${part1()}")
        println("Part2: ${part2()}")
    }
}

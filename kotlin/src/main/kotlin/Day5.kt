class Day5 : Day(5) {
    override val title = "Binary Boarding"

    private val seats = inputLines.map { line ->
        line
                .replace('F', '0')
                .replace('B', '1')
                .replace('L', '0')
                .replace('R', '1')
                .toInt(2)
    }.sorted()

    override fun part1(): Int = seats.last()

    override fun part2(): Int {
        seats.zipWithNext { l, r ->
            if (l + 1 != r) return l + 1
        }
        return 0
    }
}
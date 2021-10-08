class Day13 : Day(13) {
    override val title = "Shuttle Search"

    private val earliestTimestamp = inputLines[0].toInt()
    private val buses = inputLines[1].split(',').filter { it != "x" }.map { it.toInt() }

    override fun part1(): Int {
        var result = 0
        var earliestArrival = Integer.MAX_VALUE

        for (bus in buses) {
            val rest = earliestTimestamp % bus
            val arrivesIn = bus - rest

            if (arrivesIn < earliestArrival) {
                result = bus * arrivesIn
                earliestArrival = arrivesIn
            }
        }

        return result
    }

    override fun part2(): Any {
        TODO("Not yet implemented")
    }
}
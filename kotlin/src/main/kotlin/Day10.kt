class Day10 : Day(10) {
    override val title = "Adapter Array"

    val input = inputInts.sorted().toMutableList()

    override fun part1(): Int {
        input.add(0, 0)
        input.add(input.size, input.maxOf { it } + 3)

        val one = input.neighborDifferences(1)
        val three = input.neighborDifferences(3)
        return one * three
    }

    override fun part2(): Long {
        val paths = mutableMapOf(0 to 1L).withDefault { 0 }
        for (targetJolt in input.slice(1 until input.size)) {
            paths[targetJolt] = listOf(1,2,3).map { diff -> paths.getValue(targetJolt - diff) }.sum()
        }
        return paths[input.last()]!!
    }

}

fun MutableList<Int>.neighborDifferences(diff: Int): Int = zipWithNext().count{(first, second) -> second - first == diff}

import kotlin.streams.toList

class Day6 : Day(6) {
    override val title = "Custom Customs"

    private val inputGroups: List<List<Set<Char>>> = inputString.split("\n\n")
            .map { it.split('\n').map { it.toCharArray().toSet() } }

    override fun part1(): Any =
            inputGroups.sumBy { it.reduce { acc, line -> acc union line}.count() }

    override fun part2(): Any =
            inputGroups.sumBy { it.reduceAndCount { acc, set -> acc intersect set } }

     private fun List<Set<Char>>.reduceAndCount(op: (acc: Set<Char>, set: Set<Char>) -> Set<Char>): Int =
        reduce(op).count()
}
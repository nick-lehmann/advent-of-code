import java.util.*

class Day9 : Day(9) {
    override val title = "Encoding Error"
    private val queueLength = 25

    private val input = inputLines.map { it.toLong() }

    override fun part1(): Long =
        input.windowed(26, 1)
                .first { !it.isValid() }
                .last()

    override fun part2(): Long {
        val weakness = part1()
        var start = 0
        var end = 0
        var currentSum = 0L

        while (end < input.size) {
            when {
                currentSum < weakness -> {
                    currentSum += input[end]
                    end += 1
                }
                currentSum > weakness -> {
                    currentSum -= input[start]
                    start += 1
                }
                currentSum == weakness -> {
                    return input.slice(start until end).sorted().let { it.first() + it.last()}
                }
            }
        }
        return 0
    }
}

fun List<Long>.isValid(): Boolean {
    val desired = last()
    val base = slice(0 until size-1)
    for (element1 in base) {
        for (element2 in base) {
            if (element1 + element2 == desired && element1 != element2)
                return true
        }
    }
    return false
}
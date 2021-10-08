class Day14 : Day(14) {
    override val title = "Rambunctious Recitation"

//    private val turns = mutableListOf(0,14,1,3,7,9)
    private val turns = mutableListOf(0,3,6)

    override fun part1(): Any {
        var currentTurn = turns.size + 1
        var currentNumber = turns.last()

        while (currentTurn <= 2020) {
            val mostRecentIndex = turns.slice(0 until turns.size - 2).indexOfLast { it == currentNumber } + 1

            if (mostRecentIndex > 0) {
                currentNumber = currentTurn - mostRecentIndex - 1
            } else {
                currentNumber = 0
            }

            println("Turn $currentTurn: $currentNumber")

            turns.add(currentNumber)
            currentTurn++
        }
        return currentNumber
    }

    override fun part2(): Any {
        TODO("Not yet implemented")
    }
}
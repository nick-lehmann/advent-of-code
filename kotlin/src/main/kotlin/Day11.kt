class Day11 : Day(11) {
    override val title = "Seating System"

    private var seats: Map<Pair<Int, Int>, Seat> = mapOf()
    private val columnIndices = 0 until (inputLines.maxOfOrNull { it.length } ?: 0)
    private val rowIndices = inputLines.indices

    private fun readSeats(seeFurther: Boolean): Map<Pair<Int, Int>, Seat> {
        val seats = mutableMapOf<Pair<Int, Int>, Seat>()
        for ((row, line) in inputLines.withIndex())
            for ((column, place) in line.toCharArray().withIndex()) {
                if (place == 'L') seats[Pair(row, column)] = Seat(State.Empty, State.Occupied, mutableListOf())
                if (place == '#') seats[Pair(row, column)] = Seat(State.Occupied, State.Occupied, mutableListOf())
            }

        for ((coordinates, seat) in seats.entries) {
            val (row, column) = coordinates
            for (rowStep in -1..1) {
                for (columnStep in -1..1) {
                    if (rowStep == 0 && columnStep == 0) continue
                    var currentRow = row + rowStep
                    var currentColumn = column + columnStep
                    while (currentRow in rowIndices && currentColumn in columnIndices) {
                        val neighbour = seats[Pair(currentRow, currentColumn)]
                        if (neighbour != null) {
                            seat.neighbours.add(neighbour)
                            break
                        }
                        if (!seeFurther) break
                        currentColumn += columnStep
                        currentRow += rowStep
                    }
                }
            }
        }
        return seats
    }

    private fun iterate(threshold: Int): Boolean {
        for (seat in seats.values) {
            seat.nextState = seat.state
            if (seat.state == State.Occupied && seat.neighbours.count { it.state == State.Occupied } >= threshold)
                seat.nextState = State.Empty
            if (seat.state == State.Empty && seat.neighbours.count { it.state == State.Occupied } == 0)
                seat.nextState = State.Occupied
        }

        if (seats.values.all { it.state == it.nextState }) return false

        seats.shiftState()

        return true
    }

    private fun printGrid() {
        for (row in rowIndices) {
            for (column in columnIndices) {
                val seat = seats[Pair(row, column)]
                when (seat?.state) {
                    State.Occupied -> print('#')
                    State.Empty -> print('L')
                    else -> print('.')
                }
            }
            print('\n')
        }
    }

    override fun part1(): Int {
//        seats = readSeats(false)
//        while (iterate(4)) {
//        }
//        return seats.countOccupied()
        return 0
    }

    override fun part2(): Any {
        println("Part2")
        var currentIteration = 1
        seats = readSeats(true)
        while (iterate(5)) {
            println("Iteration $currentIteration: ${seats.countOccupied()} occupied")
            printGrid()
            currentIteration++
        }
        return seats.countOccupied()
    }
}

fun Map<Pair<Int, Int>, Seat>.countOccupied(): Int = values.count { it.state == State.Occupied }

fun Map<Pair<Int, Int>, Seat>.shiftState() {
    for (seat in this.values)
        seat.state = seat.nextState
}

class Seat(var state: State, var nextState: State, var neighbours: MutableList<Seat>)

enum class State {
    Occupied,
    Empty
}
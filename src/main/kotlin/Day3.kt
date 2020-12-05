import java.awt.Point

class Day3 : Day(3) {
    override val title = "Toboggan Trajectory"

    private fun findTrees(input: List<String>, slope: Point): Long {
        val pos = Point(0, 0)
        var trees: Long = 0

        while (pos.y < input.size) {
            if (input[pos.y][pos.x].toString() == "#") trees++
            pos.x = (pos.x + slope.x) % input[pos.y].length
            pos.y += slope.y
        }

        return trees
    }

    override fun part1(): Long {
        return findTrees(inputLines, Point(3, 1))
    }

    override fun part2(): Long {
        val slopes = listOf(
                Point(1, 1),
                Point(3, 1),
                Point(5, 1),
                Point(7, 1),
                Point(1, 2))
        var trees: Long = 1
        for (slope in slopes) {
            trees *= findTrees(inputLines, slope)
        }
        return trees
    }
}
import kotlin.math.abs

class Day12 : Day(12) {
    override val title = "Rain Risk"
    private val instructions = inputLines.mapNotNull { it.toInstructionOrNull() }

    private fun solve(waypoints: Boolean): Int {
        var x = 0
        var y = 0
        var dx = if (waypoints) 10 else 1
        var dy = if (waypoints) 1 else 0
        for (instruction in instructions) {
            when (instruction) {
                is Movement.Relative -> {
                    if (waypoints) {
                        dx += instruction.dx
                        dy += instruction.dy
                    } else {
                        x += instruction.dx
                        y += instruction.dy
                    }
                }
                is Movement.Forward -> {
                    x += instruction.n * dx
                    y += instruction.n * dy
                }
                is Movement.Left -> dx = -dy.also { dy = dx }
                is Movement.Right -> dy = -dx.also { dx = dy }
                is Movement.UTurn -> dx = -dy.also { dy = -dx }
            }
        }
        return abs(x) + abs(y)
    }

    override fun part1(): Int = solve(false)

    override fun part2(): Int = solve(true)

    private sealed class Movement {
        data class Relative(val dx: Int, val dy: Int) : Movement()
        data class Forward(val n: Int) : Movement()
        object Left : Movement()
        object Right : Movement()
        object UTurn : Movement()
    }

    companion object {
        @Suppress("ComplexMethod", "ReturnCount")
        private fun String.toInstructionOrNull(): Movement? {
            return when {
                startsWith("N") -> Movement.Relative(0, drop(1).toIntOrNull() ?: return null)
                startsWith("E") -> Movement.Relative(drop(1).toIntOrNull() ?: return null, 0)
                startsWith("S") -> Movement.Relative(0, -(drop(1).toIntOrNull() ?: return null))
                startsWith("W") -> Movement.Relative(-(drop(1).toIntOrNull() ?: return null), 0)
                equals("L90") || equals("R270") -> Movement.Left
                equals("R90") || equals("L270") -> Movement.Right
                equals("L180") || equals("R180") -> Movement.UTurn
                startsWith("F") -> Movement.Forward(drop(1).toIntOrNull() ?: return null)
                else -> null
            }
        }
    }
}

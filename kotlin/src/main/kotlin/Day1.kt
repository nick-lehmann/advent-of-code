class Day1: Day(1) {
    override val title = "Report Repair"
    private val target = 2020

    override fun part1(): Int {
        for (value1 in inputInts) {
            for (value2 in inputInts) {
                if (value1 + value2 == target) { return value1 + value2 }
            }
        }
        return 0
    }

    override fun part2(): Any {
        for (value1 in inputInts) {
            for (value2 in inputInts) {
                for (value3 in inputInts) {
                    if (value1 + value2 + value3 == target) {
                        return value1 + value2 + value3
                    }
                }
            }
        }
        return 0
    }
}
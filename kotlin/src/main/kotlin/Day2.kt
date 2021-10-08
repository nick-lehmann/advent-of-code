class Day2: Day(2) {
    override val title = "Password Philosophy"

    override fun part1(): Int {
        val regex = "(\\d*)-(\\d*) (\\w): (.*)".toRegex()
        return inputLines.count {
            val match = regex.find(it)!!
            val (start, end, letter, password) = match.groups.toList().drop(1).map { it?.value }
            val count = password?.count { letter?.contains(it) ?: false }!!
            start!!.toInt() <= count && count <= end!!.toInt()
        }
    }

    override fun part2(): Int {
        return inputLines.count {
            val regex = "(\\d*)-(\\d*) (\\w): (.*)".toRegex()
            val match = regex.find(it)!!
            val (first, second, letter, password) = match.groups.toList().drop(1).map { it!!.value }

            try {
                (password.elementAt(first.toInt() - 1) == letter.elementAt(0)) xor
                        (password.elementAt(second.toInt() - 1) == letter.elementAt(0))
            } catch (e: StringIndexOutOfBoundsException) {
                false
            }
        }
    }

}
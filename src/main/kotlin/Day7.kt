class Day7 : Day(7) {
    override val title = "Handy Haversacks"

    private val linePattern = """(\w+ \w+) bags contain (.*)""".toRegex()
    private val singleItemPattern = """(\d+) (\w+ \w+) bags?""".toRegex()

    private val input: Map<String, Map<String, Int>> = inputLines.associate { line ->
        val (key, items) = linePattern.matchEntire(line)!!.destructured
        key to singleItemPattern.findAll(items).associate { match ->
            val (count, name) = match.destructured
            name to count.toInt()
        }
    }

    override fun part1(): Int {
        val canContainGold = mutableMapOf<String, Lazy<Boolean>>()
        for ((key, items) in input.entries) {
            canContainGold[key] = lazy {
                items.keys.any { name ->
                    name == "shiny gold" || canContainGold[name]?.value == true
                }
            }
        }
        return canContainGold.values.count { it.value }
    }

    override fun part2(): Int {
        return insideBags("shiny gold") - 1
    }

    private fun insideBags(name: String): Int =
        input.getOrElse(name) { return 1 }.entries.map { (name, quantity) -> quantity * insideBags(name) }.sum() + 1
}

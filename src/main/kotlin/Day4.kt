class Day4 : Day(4) {
    override val title = "Passport Processing"
    private val requiredFields = listOf("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")

    private fun countValidPassports(criteria: List<(passport: Map<String, String>) -> Boolean>): Int =
            passports().count { passport -> criteria.map { it(passport) }.all { it } }

    private fun passports(): Sequence<Map<String, String>> = sequence {
        for (passport in inputString.split("\n\n")) {
            val map = mutableMapOf<String, String>()
            passport.replace('\n', ' ').split(' ').map {
                val (key, value) = it.split(':')
                map[key] = value
            }
            yield(map)
        }
    }

    override fun part1(): Int =
            countValidPassports(listOf { passport -> passport.keys.containsAll(requiredFields) })

    override fun part2(): Int =
            countValidPassports(listOf(
                    { p -> (1920..2002).contains(p["byr"]?.toInt()) },
                    { p -> (2010..2020).contains(p["iyr"]?.toInt()) },
                    { p -> (2020..2030).contains(p["eyr"]?.toInt()) },
                    { p ->
                        when (p["hgt"]?.takeLast(2)) {
                            "cm" -> (p["hgt"]?.dropLast(2)?.toInt() ?: 0) in 150..193
                            "in" -> (p["hgt"]?.dropLast(2)?.toInt() ?: 0) in 56..76
                            else -> false
                        }
                    },
                    { p -> p["hcl"]?.matches("#[0-9a-f]{6}".toRegex()) ?: false },
                    { p -> listOf("amb", "blu", "brn", "gry", "grn", "hzl", "oth").contains(p["ecl"]) },
                    { p -> p["pid"]?.matches("\\d{9}".toRegex()) ?: false }
            ))
}
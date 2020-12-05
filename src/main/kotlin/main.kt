import java.io.File

fun main(args: Array<String>) {
    val day = Day5()
    day.run()
}

fun getResource(name: String): List<String> {
    val content = File("src/main/resources/$name").readText()
    return content.split('\n').filter { it != "" }
}

/**
 * Exercise 01
 * https://adventofcode.com/2020/day/1
 */
fun reportRepair() {
    val input = getResource("01.txt").map { it.toInt() }
    val target = 2020

    // Part 1
    for (value1 in input) {
        for (value2 in input) {
            if (value1 + value2 == target) {
                println("$value1 + $value2 == $target")
                println("$value1 * $value2 == ${value1 * value2}")
                return
            }
        }
    }


    // Part 2
    for (value1 in input) {
        for (value2 in input) {
            for (value3 in input) {
                if (value1 + value2 + value3 == target) {
                    println("$value1 + $value2 + $value3 == $target")
                    println("$value1 * $value2 * $value3 == ${value1 * value2 * value3}")
                    return
                }
            }
        }
    }
}


/**
 * Exercise 02
 * https://adventofcode.com/2020/day/2
 */
fun passwordPhilosophy() {
    val input = getResource("02.txt")

    // Part 1
    print(input.count {
        val regex = "(\\d*)-(\\d*) (\\w): (.*)".toRegex()
        val match = regex.find(it)!!
        val (start, end, letter, password) = match.groups.toList().drop(1).map { it?.value }
        val count = password?.count { letter?.contains(it) ?: false }!!
        start!!.toInt() <= count && count <= end!!.toInt()
    })

    // Part 2
    print(input.count {
        val regex = "(\\d*)-(\\d*) (\\w): (.*)".toRegex()
        val match = regex.find(it)!!
        val (first, second, letter, password) = match.groups.toList().drop(1).map { it!!.value }

        try {
            (password.elementAt(first.toInt() - 1) == letter.elementAt(0)) xor
                    (password.elementAt(second.toInt() - 1) == letter.elementAt(0))
        } catch (e: StringIndexOutOfBoundsException) {
            false
        }
    })
}

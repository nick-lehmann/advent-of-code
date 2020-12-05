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
}



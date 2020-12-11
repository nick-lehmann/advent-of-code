class Day8 : Day(8) {
    override val title = "Handheld Halting"

    private val program = inputLines.map { line ->
        val (instruction, argument) = line.split(" ")
        Instruction(Op.valueOf(instruction), argument.toInt())
    }

    override fun part1(): Int {
        val vm = VirtualMachine(program)
        val visited = mutableSetOf<Int>()
        while (visited.add(vm.pointer))
            vm.step()
        return vm.accumulator
    }

    override fun part2(): Int {
        program.forEachIndexed { index, instruction ->
            val vm = when(instruction.op) {
                Op.jmp -> {
                    val newCode = program.toMutableList()
                    newCode[index] = Instruction(Op.nop, instruction.argument)
                    VirtualMachine(newCode)
                }
                Op.nop -> {
                    val newCode = program.toMutableList()
                    newCode[index] = Instruction(Op.jmp, instruction.argument)
                    VirtualMachine(newCode)
                }
                else -> null
            }
            if (vm?.hasLoop() == false) return vm.accumulator
        }
        return -1
    }
}

class VirtualMachine(private val program: List<Instruction>) {
    var pointer = 0
    var accumulator = 0

    fun hasLoop(): Boolean {
        val visited = mutableSetOf<Int>()
        do {
            if (!visited.add(pointer)) return true
        } while (step())
        return false
    }

    fun step(): Boolean {
        if (pointer !in program.indices) return false
        val instruction = program[pointer]
        when (instruction.op) {
            Op.jmp -> pointer += instruction.argument
            Op.acc -> {
                accumulator += instruction.argument
                pointer++
            }
            Op.nop -> pointer++
        }
        return true
    }
}


data class Instruction(val op: Op, val argument: Int)

enum class Op {
    nop,
    acc,
    jmp
}
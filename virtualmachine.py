from enum import Enum
from logging import info, debug, warn, error, critical
from typing import List

from parser import ArgType, Instruction, Registers


class Dynacall:
    def __init__(self, registers: list[int], pc: int) -> None:
        self.registers: list[int] = registers
        self.pc: int = pc

    def vm_add(self, instruction: Instruction) -> None:
        for arg in instruction.args:
            if arg.type is ArgType.VALUE:
                self.registers[Registers.byName(
                    instruction.args[0].value)] += int(arg.value)

    def vm_sub(self, instruction: Instruction) -> None:
        for arg in instruction.args:
            if arg.type is ArgType.VALUE:
                self.registers[Registers.byName(
                    instruction.args[0].value)] -= int(arg.value)

    def vm_inc(self, instruction: Instruction) -> None:
        for arg in instruction.args:
            if arg.type is ArgType.VALUE:
                self.registers[Registers.byName(
                    instruction.args[0].value)] += 1

    def vm_dec(self, instruction: Instruction) -> None:
        for arg in instruction.args:
            if arg.type is ArgType.VALUE:
                self.registers[Registers.byName(
                    instruction.args[0].value)] -= 1

    def vm_prnt(self, instruction: Instruction) -> None:
        print(self.registers[Registers.byName(instruction.args[0].value)])

    def vm_dbg(self, instruction: Instruction) -> None:
        print(
            f"\n\nDEBUG PRINT REQUESTED BY PROGRAM AT LINE {self.pc + 1}\nDUMPING REGISTERS\n", end="")
        for i in range(0, len(self.registers)):
            print(f"  {Registers(i).name}: {self.registers[i]}")
        print(f"PC: {self.pc}")


class VM:
    def __init__(self) -> None:
        self.registers: list[int] = [0, 0, 0, 0, 0, 0, 0, 0]  # 8 Registers
        self.pc: int = 0

    def run(self, instructions: list[Instruction]) -> None:
        ddt = Dynacall(self.registers, self.pc)
        for instr in instructions:
            try:
                getattr(ddt, 'vm_%s' % instr.op.lower())(instr)
                ddt.pc += 1
                self.pc = ddt.pc
                self.registers = ddt.registers
            except AttributeError:
                critical(
                    f"Illegal instruction '{instr.op}' on line {self.pc}. Aborting...")
                quit(-1)

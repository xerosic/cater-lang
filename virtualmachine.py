from enum import Enum
import logging
from logging import info, debug, warn, error, critical
from typing import List

class Registers(Enum):
    EAX = 0
    EBX = 1
    ECX = 2
    EDX = 3
    AX = 4
    BX = 5
    CX = 6
    DX = 7

    def byName(name: str) -> int:
        return Registers[name].value
    def list() -> List:
        return [x.name for x in Registers]



class VM:
    def __init__(self) -> None:
        self.registers = [0, 0, 0, 0, 0, 0, 0, 0]  # 8 Registers
        self.pc: int = 0

        debug(Registers.list())

    def run(self, instructions: str) -> None:
        for instr in instructions:
            match instr[0].lower():
                case "add":
                    for i in range(2, len(instr)):
                        self.registers[Registers.byName(
                            instr[1].upper())] += int(instr[i])
                case "sub":
                    for i in range(2, len(instr)):
                        self.registers[Registers.byName(
                            instr[1].upper())] -= int(instr[i])
                case "inc":
                    for i in range(2, len(instr)):
                        self.registers[Registers.byName(instr[1].upper())] += 1
                case "dec":
                    for i in range(2, len(instr)):
                        self.registers[Registers.byName(instr[1].upper())] -= 1
                case "prnt":
                    print(self.registers[Registers.byName(instr[1].upper())])
                case "dbg":
                    print(
                        f"\n\nDEBUG PRINT REQUESTED BY PROGRAM AT LINE {self.pc + 1}\nDUMPING REGISTERS\n\n", end="")
                    for i in range(0, len(self.registers)):
                        print(f"  {Registers(i).name}: {self.registers[i]}")
                    print(f"  PC: {self.pc}")
            self.pc += 1

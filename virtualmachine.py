from enum import Enum
import logging

class Registers(Enum):
    EAX = 0
    EBX = 1
    ECX = 2
    EDX = 3
    AX = 4
    BX = 5
    CX = 6
    DX = 7


class VM:
    def __init__(self) -> None:
        self.registers = [0, 0, 0, 0, 0, 0]  # 6 Registers
        self.pc: int = 0

    def run(self, instructions: str) -> None:
        for instr in instructions:
            match instr[0].lower():
                case "add":
                    for i in range(2, len(instr)):
                        self.registers[Registers[instr[1].upper()
                                                 ].value] += int(instr[i])
                case "sub":
                    for i in range(2, len(instr)):
                        self.registers[Registers[instr[1].upper()
                                                 ].value] -= int(instr[i])
                case "inc":
                    for i in range(2, len(instr)):
                        self.registers[Registers[instr[1].upper()
                                                 ].value] += 1
                case "dec":
                    for i in range(2, len(instr)):
                        self.registers[Registers[instr[1].upper()
                                                 ].value] -= 1                                                 
                case "prnt":
                    print(self.registers[Registers[instr[1].upper()].value])

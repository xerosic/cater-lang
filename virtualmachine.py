from enum import Enum
from multiprocessing import Value

class Registers(Enum):
    RAX = 0
    RBX = 1
    RCX = 2
    RDX = 3
    REX = 4
    RFX = 5

class VM:
    def __init__(self) -> None:
        self.registers = [0, 0, 0, 0, 0, 0] # 6 Registers
        self.pc: int = 0
    def run(self, instructions: str) -> None:
        for instr in instructions:
            match instr[0].lower():
                case "add":
                    for i in range(2, len(instr)):
                        self.registers[Registers[instr[1].upper()].value] += int(instr[i])
                case "prnt":
                    print("[OUT] : ", self.registers[Registers[instr[1].upper()].value])
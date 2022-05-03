
class VM:
    def __init__(self) -> None:
        self.registers = [0, 0, 0, 0, 0, 0, 0, 0] # 8 Registers
        self.pc = 0
    def run(self, instructions: str) -> None:
        raise NotImplementedError
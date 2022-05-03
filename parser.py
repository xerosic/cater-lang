from typing import List


class Parser:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
    def parseFile(self) -> None:
        self.file = open(self.file_name, "R").readlines()
    def parseInstructions(self) -> List:
        self.instructions = []
        for line in self.file:
            self.instructions.append(line.split(" "))


from typing import List
from logging import info, debug, warn, error, critical


class Parser:
    def __init__(self, file_name: str) -> None:
        try:
            open(file=file_name)
        except FileNotFoundError:
            critical(f"The provided file ({file_name}) does not exist or cannot be read.")

        self.file_name = file_name
        info(f"Parser: file loaded ({file_name}).")


    def parseFile(self) -> None:
        self.file = open(self.file_name, "r").readlines()
        self.parseInstructions()

    def parseInstructions(self) -> None:
        self.instructions = []
        for line in self.file:
            self.instructions.append(line.split(" "))

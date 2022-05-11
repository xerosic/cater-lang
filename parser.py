from enum import Enum
from os import path
from typing import List
from logging import info, debug, warn, error, critical


class ArgType(Enum):
    REG = 0
    MEM = 1
    VALUE = 2


class Argument:
    def __init__(self, arg: str) -> None:
        pass

    def determineType(self, arg: str) -> None:
        pass


class Instruction:
    def __init__(self, line: str) -> None:
        self.sanitize(line)

    def parseBaseInstruction(self):
        self.op = ""
        for c in self.sanitized:
            if c is not ' ':
                self.op += c
            else:
                break

    def sanitize(self, line: str):
        self.sanitized = line.replace("\n", "")


class Parser:
    def __init__(self, file_name: str) -> None:
        if not path.exists(file_name):
            critical(
                f"The provided file ({file_name}) does not exist or cannot be read.")

        self.file_name = file_name
        info(f"[parser] file loaded ({file_name}).")

    def parseFile(self) -> None:
        self.file = open(self.file_name, "r").readlines()
        info(
            f"[parser] file opened ({self.file_name}) ({len(self.file)} lines).")
        info(f"[parser] started parsing ({self.file_name}).")
        self.parseInstructions()

    def parseInstructions(self) -> None:
        self.instructions = []
        for line in self.file:
            self.instructions.append(line.replace("\n", "").split(" "))

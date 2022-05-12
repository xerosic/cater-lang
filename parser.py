from enum import Enum
from os import path
from typing import List
from logging import info, debug, warn, error, critical

from virtualmachine import Registers


class ArgType(Enum):
    REG = 0
    MEM = 1
    VALUE = 2


class Argument:
    def __init__(self, arg: str) -> None:
        pass

    def determineType(self, arg: str) -> None:
        if arg in Registers.list():
            self.type = ArgType.REG
        if arg.isnumeric():
            self.type = ArgType.VALUE


class Instruction:
    def __init__(self, line: str) -> None:
        self.line = line
        self.parseBaseInstruction()
        self.parseArguments()
        debug(self.op)
        #debug(self.args[0])

    def parseBaseInstruction(self):
        self.op = ""
        for c in self.line:
            if c is not ' ':
                self.op += c
            else:
                break
    
    def parseArguments(self):
        self.args: List = []
        self.argbuffer: str = ""
        self.argumentLine: str = self.line.replace(self.op, "").replace("\n", "")

        for c in self.argumentLine:
            if c is ' ':
                self.argumentLine.removeprefix

        for c in self.argumentLine:
            if c is not ' ':
                self.argbuffer += c
                debug(f"Added char '{c}' in '{self.argbuffer}'")
            else:
                debug(f"Argument: {self.argbuffer}")
                self.args.append(Argument(self.argbuffer))
                self.argbuffer = ""

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
            Instruction(line)
            self.instructions.append(line.replace("\n", "").split(" "))

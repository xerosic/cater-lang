from enum import Enum
from os import path
from typing import List
from logging import info, debug, warn, error, critical


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


class ArgType(Enum):
    REG = 0
    MEM = 1
    VALUE = 2
    VIRT = 3


class Argument:
    def __init__(self, arg: str) -> None:
        self.determineType(arg)
        self.value = arg

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
        self.argLine: str = self.line.replace(
            self.op, "").replace("\n", "").strip()

        debug(self.argLine)

        for c in self.argLine:
            if c is not ' ':
                self.argbuffer += c
            else:
                debug(f"argBuffer: {self.argbuffer}")
                self.args.append(Argument(self.argbuffer))
                self.argbuffer = ""

        for arg in self.args:
            debug(f"Loaded argument: '{arg.value}' ({arg.type})")


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

        info("[parser] injecting virtual arguments")

        for line in self.file:
            self.instructions.append(Instruction(line + " ^"))

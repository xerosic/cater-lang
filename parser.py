
from typing import List


class Parser:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
    def parseFile(self) -> None:
        self.file = open(self.file_name, "R").readlines()
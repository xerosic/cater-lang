import parser, virtualmachine

def banner():
    print("              __           ")
    print("  _________ _/ /____  _____")
    print(" / ___/ __ `/ __/ _ \/ ___/")
    print("/ /__/ /_/ / /_/  __/ /    ")
    print("\___/\__,_/\__/\___/_/     ")
    print("                           ")

banner()

fileParser = parser.Parser("main.bo")
fileParser.parseFile()

vm = virtualmachine.VM()

vm.run(fileParser.instructions)
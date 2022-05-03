import parser, virtualmachine

print("Bazonga interpreter v0.1")

parser = parser.Parser("main.bo")

vm = virtualmachine.VM()

vm.run()
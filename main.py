import logging
import parser
import virtualmachine
import utils

import argparse

argparser = argparse.ArgumentParser(description=utils.banner())
argparser.add_argument('file', metavar='input_file', type=str,
                    help='the .ct source file to be interpreted')
argparser.add_argument('--log', type=str, metavar='level', help='the level of the logger that should be set. default: WARN')

args = argparser.parse_args()
if args.log is not None: utils.setLogLevel(args.log)

fileParser = parser.Parser(args.file)
fileParser.parseFile()

vm = virtualmachine.VM()

vm.run(fileParser.instructions)

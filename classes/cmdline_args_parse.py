# MIT License
#
# Copyright (c) 2022 SD Card Coverter
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# @author: DawsonXBancroft
import os.path
import sys
from verbosity import *
class CMDLineParser:

    def __init__(self):
        self.verbosity = Verbosity.MEDIUM
        self.input_file_path = "null"
        self.config_file_path = "null"
        self.output_file_path = "null"
        self.datapoints = 0
        self.gui = False
        self.usage = "Usage: main.py -inputfile <PATH> -type <{DEBUG, NO_ATTACH, NEMO}> [-outputfile <PATH>] [-verb" \
            "osity [<LOW, MEDIUM, HIGH, DEBUG}>] [-gui]] "

    def parse(self):
        args = sys.argv[1:]
        if len(args) == 0:
            print(usage)
            sys.exit()
        for i in range(0, len(args), 1):
            if args[i] == "-verbosity":
                if args[i + 1] == "HIGH":
                    self.verbosity = Verbosity.HIGH
                    i = i + 1
                elif args[i + 1] == "MEDIUM":
                    self.verbosity = Verbosity.MEDIUM
                    i = i + 1
                elif args[i + 1] == "LOW":
                    self.verbosity = Verbosity.LOW
                    i = i + 1
                elif args[i + 1] == "DEBUG":
                    self.verbosity = Verbosity.DEBUG
                    i = i + 1
                else:
                    print("FATAL: VERBOSITY IS INVALID")
                    print("       Please use -verbosity [LOW, MEDIUM, HIGH, DEBUG]")
                    sys.exit()
            elif args[i] == "-inputfile":
                if os.path.exists(args[i + 1]):
                    self.input_file_path = args[i + 1]
                    i = i + 1
                else:
                    print("FATAL: INPUT FILE DOES NOT EXIST")
                    print("       Please ensure filepath is correct and the file exists.")
                    sys.exit()
            elif args[i] == "-outputfile":
                if os.path.exists(args[i + 1]):
                    usr_input = input("File " + args[i + 1] + " exists. Would you like to overwrite it? (y/n)")
                    if usr_input.lower() == "y":
                        self.output_file_path = args[i + 1]
                        i = i + 1
                    else:
                        print("Okay; Exiting program")
                        sys.exit()
                else:
                    self.output_file_path = args[i + 1]
                    i = i + 1
            elif args[i] == "-datapoints":
                self.datapoints = int(args[i + 1])
                i = i + 1
            elif args[i] == "-type":
                if args[i + 1].upper() == "DEBUG":
                    self.config_file_path = "config/debug.yaml"
                    i = i + 1
                else:
                    print("FATAL: NO TYPE FOUND FOR " + args[i + 1])  # TODO: REPLACE WITH STD FILE
                    sys.exit()
            elif args[i] == "-gui":
                self.gui = True

        if self.verbosity.value > Verbosity.HIGH.value:
            print("\nEND OF PARSING ARGUMENTS")
            print("    verbosity     : " + self.verbosity.name)
            print("    gui           : " + str(self.gui))
            print("    input file    : " + self.input_file_path)
            print("    output file   : " + self.output_file_path)
            print("    type          : " + self.config_file_path)
            print("    datapoints    : " + str(self.datapoints))
            print()

        if not self.gui:
            if self.input_file_path == "null":
                print("FATAL: INPUT FILE NOT SPECIFIED")
                print(usage)
                sys.exit()
            if self.config_file_path == "null":
                print("FATAL: TYPE NOT SPECIFIED")
                print(usage)
                sys.exit()

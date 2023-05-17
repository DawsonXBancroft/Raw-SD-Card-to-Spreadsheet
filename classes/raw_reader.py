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
import sys
from verbosity import *
from yaml_config import *
from transaction import *
class RawReader:

    def __init__(self):
        self.verbosity = Verbosity.MEDIUM
        self.input_file_path = "null"
        self.f = "null"
        self.cfg = "null"
        self.writer = "null"
        self.datapoints = 0

    def openFile(self):
        self.f = open(self.input_file_path, 'r')

    def closeFile(self):
        # check to see if file is open
        if self.f == "null":
            print("\nFATAL: FILE NOT OPEN, PLEASE OPEN THE FILE BEFORE CLOSING IT")
            sys.exit()
        # close file
        self.f.close()
        if self.verbosity.value > Verbosity.HIGH.value:
            print("Closed file: " + self.input_file_path)


    def readStart(self):
        self.readBlock(0)
        print("block 0 read")
        self.readBlock(1)
        print("block 1 read")

    def readBlock(self, block_number):
        # check to see if file is open
        if self.f == "null":
            print("\nFATAL: FILE NOT OPEN, PLEASE ENSURE FILE PATH IS CORRECT")
            sys.exit()

        # generate a new transaction
        trx = Transaction()

        # seek to the block_number
        self.f.seek((block_number*78*32), 0) # 78 is # of chars, next 32 is number of lines

        line = self.f.readline()

        for i in range(31): # number of lines in a SD card readBlock
            line = self.f.readline() # read the line
            # print(line) debug statement

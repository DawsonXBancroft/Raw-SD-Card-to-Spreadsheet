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
from transaction import *
class RawReader:

    def __init__(self):
        self.verbosity = Verbosity.MEDIUM
        self.input_file_path = "null"
        self.f = "null"

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

    def readBlock(self):
        # check to see if file is open
        if self.f == "null":
            print("\nFATAL: FILE NOT OPEN, PLEASE OPEN THE FILE BEFORE CLOSING IT")
            sys.exit()

        # generate a new transaction
        trx = Transaction()

        # get first pointer for beginning of file
        lastLinePtr = self.f.tell()
        lastLine_address = 0

        for i in range(20): # 20 lines per block default

            # read in line
            line = self.f.readline()

            # break line up, delimited by spaces
            line_chunks = line.split(' ')

            # if line chunks 0 == * read the next line after
            if line_chunks[0] == '*':
                nextLine = self.f.readline()
                nextLine_chunks = nextLine.split(' ')
                nextLine_address = int(nextLine_chunks)
            else:


        # line = self.f.readline()
        # print(line)
        # trx.verbosity = self.verbosity

        # self.f.seek(lastLinePtr, 0)
        # print(line)


        # if verbosity is greater than HIGH print out debug info
        if self.verbosity.value > Verbosity.HIGH.value:
            print("\n\nRawReader read this block: " +
                  "\nand generated this transaction:" + trx.convert2string())
        return trx

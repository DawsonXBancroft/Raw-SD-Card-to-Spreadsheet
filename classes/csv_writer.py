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
import csv
from datetime import datetime
from verbosity import *
class CSVWriter:

    def __init__(self):
        self.verbosity = Verbosity.MEDIUM
        self.output_file_path = "null"
        self.f = "null"
        self.writer = "null"

    def openCSVFile(self):
        # check to see if output_file_path is specified
        if self.output_file_path == "null":
            self.output_file_path = datetime.now().strftime("OutputFiles/%Y_%m_%d-%I_%M_%S_%p.csv")
        # open file in write mode
        self.f = open(self.output_file_path, 'w')
        # create a csv writer
        self.writer = csv.writer(self.f)
        if self.verbosity.value > Verbosity.HIGH.value:
            print("\nOpened file: " + self.output_file_path)

    def closeCSVFile(self):
        # check if file is open
        if self.f == "null":
            print("\nFATAL: FILE NOT OPEN, PLEASE OPEN THE FILE BEFORE CLOSING IT")
            sys.exit()
        # close file
        self.f.close()
        if self.verbosity.value > Verbosity.HIGH.value:
            print("Closed file: " + self.output_file_path)

    def writeHeaders(self, header):
        # check if file is open
        if self.f == "null":
            print("\nFATAL: FILE NOT OPEN, PLEASE OPEN THE FILE BEFORE WRITING TO IT")
            sys.exit()
        # write to the file
        self.writer.writerow(header)
        if self.verbosity.value > Verbosity.HIGH.value:
            print("\nPrinted " + str(header) + " in csv file")

    def writeData(self, data):
        # check if file is open
        if self.f == "null":
            print("\nFATAL: FILE NOT OPEN, PLEASE OPEN THE FILE BEFORE WRITING TO IT")
            sys.exit()
        # write to the file
        self.writer.writerow(data)
        if self.verbosity.value > Verbosity.HIGH.value:
            print("\nPrinted " + str(data) + " in csv file")


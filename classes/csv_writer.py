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
            print("Opened file: " + self.output_file_path)

    def closeCSVFile(self):
        # check if file is open
        if self.f == "null":
            print("FATAL: FILE NOT OPEN, PLEASE OPEN THE FILE BEFORE CLOSING IT")
            sys.exit()
        # close file
        self.f.close()
        if self.verbosity.value > Verbosity.HIGH.value:
            print("Closed file: " + self.output_file_path)

    def writeHeaders(self, header):
        # check if file is open
        if self.f == "null":
            print("FATAL: FILE NOT OPEN, PLEASE OPEN THE FILE BEFORE WRITING TO IT")
            sys.exit()
        # write to the file
        self.writer.writerow(header)
        if self.verbosity.value > Verbosity.HIGH.value:
            print("Printed " + str(header) + " in csv file")

    def writeData(self, data):
        # check if file is open
        if self.f == "null":
            print("FATAL: FILE NOT OPEN, PLEASE OPEN THE FILE BEFORE WRITING TO IT")
            sys.exit()
        # write to the file
        self.writer.writerow(data)
        if self.verbosity.value > Verbosity.HIGH.value:
            print("Printed " + str(data) + " in csv file")


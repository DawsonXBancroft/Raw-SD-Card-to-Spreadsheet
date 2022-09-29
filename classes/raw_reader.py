# @author: DawsonXBancroft
import sys
from verbosity import *
class RawReader:

    def __init__(self):
        self.verbosity = Verbosity.MEDIUM
        self.input_file_path = "null"
        self.f = "null"

    def openFile(self):
        self.f = open(input_file_path, 'r')

    def closeFile(self):
        self.f.close()

    def readLine(self):
        line = self.f.readlime()
        return line

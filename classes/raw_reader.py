# @author: DawsonXBancroft
import sys
from verbosity import *
class RawReader:

    def __init__(self):
        self.verbosity = Verbosity.MEDIUM
        self.input_file_path = "null"
        self.f = "null"

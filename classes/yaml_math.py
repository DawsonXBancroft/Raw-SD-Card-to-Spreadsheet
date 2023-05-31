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
from transaction import *
from yaml_config import *
from verbosity import *
class YamlMath:

    def __init__(self):
        self.verbosity = Verbosity.MEDIUM
        self.block_arr = []
        self.yaml_cfg = YamlConfig()
        self.config_data = []
        self.config_dic = {}

    def do_config_math(self):
        if len(block_arr) == 0:
            if self.verbosity.value > Verbosity.HIGH.value:
                print("\nNo blocks added for the config. Skipping config data (if any)\n")
        else:
            if self.verbosity.value > Verbosity.HIGH.value:
                print("\nDetected " + str(len(block_arr)) + " blocks of config data.\n")
            for i in range(len(block_arr)):
                # for each block
                    # for each item in the dictionary
                        # make an entry in this diectionary with the configuration data
        # calculate the config data and store it

    def add_to_block_array(self, block):
        self.block_arr.append(block)
        #print(self.block_arr[-1].block_number)

   # def do_math(self):
        # check if block array is empty

        # perform math

        # empty the array

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
        self.config_dict = {}
        self.data_dict = {}

    def do_config_math(self):
        if len(block_arr) == 0:
            if self.verbosity.value > Verbosity.HIGH.value:
                print("\nNo blocks added for the config. Skipping config data (if any)\n")
        else:
            if self.verbosity.value > Verbosity.HIGH.value:
                print("\nDetected " + str(len(self.block_arr)) + " blocks of config data.\n")
            for i in range(len(block_arr)):
                for j in range(len(yaml_cfg.math_config_dict)):
                    string_temp = "CFG_" + i + ":BYTE_" + j
                    if string_temp in yaml_cfg.math_config_block_info_dict.keys():
                        config_dict[yaml_cfg.math_config_block_info_dict[string_temp]] = block.values[j]
        # calculate the config data and store it

    def do_math(self):
        if len(self.block_arr) == 0:
            if self.verbosity.value > Verbosity.HIGH.value:
                print("\nERROR: No blocks added for this data math.\n")
        else:
            if self.verbosity.value > Verbosity.HIGH.value:
                print("\nDetected " + str(len(self.block_arr)) + " blocks of actual data.\n")
            #for i in range(len(self.block_arr)):
            for i in range(self.yaml_cfg.num_data_blocks):
                for j in range(self.yaml_cfg.sd_card_setup_dict["NUM_BYTES_DB_" + str(i)]):
                    self.data_dict[self.yaml_cfg.data_block_info_dict["DB_" + str(i) + "_BYTE_" + str(j)]] = int(self.block_arr[i].values[j], 16)
        # perform math
        for col_values in self.yaml_cfg.col_vars_dict.values():
            self.evaluate_expression(self.yaml_cfg.math_data_dict[col_values])


        # empty the array and dictionary
        self.block_arr.clear()
        self.data_dict.clear()

    def add_to_block_array(self, block):
        self.block_arr.append(block)

    def evaluate_expression(self, expressionIn):
        if '(' in expressionIn:
            if ')' in expressionIn:
                expressionRecurse = expressionIn[expressionIn.find("(")+1:]
                flipped_expression = "".join(reversed(expressionRecurse))
                flipped_expression = flipped_expression[flipped_expression.find(")")+1:]
                expressionRecurse = "".join(reversed(flipped_expression))
                temp_num = self.evaluate_expression(expressionRecurse)
            else:
                print("\nFATAL: \'(\' FOUND BUT \')\' IS NOT FOUND, CHECK THE YAML CONFIG")
                sys.exit()
        elif ')' in expressionIn:
            print("\nFATAL: \')\' FOUND BUT EXPECTING \'(\' AS WELL, CHECK YAML CONFIG")
            sys.exit()


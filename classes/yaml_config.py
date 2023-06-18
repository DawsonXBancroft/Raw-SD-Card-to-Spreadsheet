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
import yaml
import sys
from verbosity import *
class YamlConfig():

    # Class for holding configuration of SD Card and CSV file


    # When constructed, the config_file_path is required
    def __init__(self):
        self.config_file_path = "null"
        self.verbosity = Verbosity.MEDIUM
        self.col_labels_dict = {}
        self.col_vars_dict = {}
        self.sd_card_setup_dict = {}
        self.config_block_info_dict = {}
        self.data_block_info_dict = {}
        self.math_config_dict = {}
        self.math_data_dict = {}
        self.num_data_blocks = 0
        self.num_config_blocks = 0

    def readInConfig(self):
        # get column labels (column headers for csv file)
        if self.verbosity.value > Verbosity.HIGH.value:
            print("\nGetting Column Labels {col_label_dict}")
        for key, value in yaml.safe_load(open(self.config_file_path))['COL_LABELS'].items():
            self.col_labels_dict[key] = value
            if self.verbosity.value > Verbosity.HIGH.value:
                print("\t" + str(key) + "\t" + str(value))



        # get column vars (variables that will go in each row of the csv file)
        if self.verbosity.value > Verbosity.HIGH.value:
            print("\nGetting Column Variables {col_vars_dict}")
        for key, value in yaml.safe_load(open(self.config_file_path))['COL_VARS'].items():
            self.col_vars_dict[key] = value
            if self.verbosity.value > Verbosity.HIGH.value:
                print("\t" + str(key) + "\t" + str(value))

        # get sd card setup
        if self.verbosity.value > Verbosity.HIGH.value:
            print("\nGetting Column SD Card Setup {sd_card_setup_dict}")
        for key, value in yaml.safe_load(open(self.config_file_path))['SDCARD_SETUP'].items():
            self.sd_card_setup_dict[key] = value
            if self.verbosity.value > Verbosity.HIGH.value:
                print("\t" + str(key) + "   \t" + str(value))

        # check to make sure necessary items were set in the yaml config file
        if not ("IMAGE_DATA" in self.sd_card_setup_dict):
            print("FATAL: IMAGE_DATA not found in sd_card_setup_dict")
            sys.exit()
        if not ("DATA_POINTS_IN_CONFIG" in self.sd_card_setup_dict):
            print("FATAL: DATA_POINTS_IN_CONFIG not found in sd_card_setup_dict")
            sys.exit()
        if not ("NUM_CONFIG_BLOCKS" in self.sd_card_setup_dict):
            print("FATAL: NUM_CONFIG_BLOCKS not found in sd_card_setup_dict")
            sys.exit()
        if not ("NUM_DATA_BLOCKS" in self.sd_card_setup_dict):
            print("FATAL: NUM_DATA_BLOCKS not found in sd_card_setup_dict")
            sys.exit()
        if not ("NUM_BYTES_DB_0" in self.sd_card_setup_dict):
            print("FATAL: NUM_BYTES_DB_0 not found in sd_card_setup_dict")
            sys.exit()
        if not ("NUM_DB_MATH_BLOCKS" in self.sd_card_setup_dict):
            print("FATAL: NUMCFG_MATH_BLOCKS not found in sd_card_setup_dict")
            sys.exit()

        # get configuration data info
        self.num_config_blocks = self.sd_card_setup_dict["NUM_CONFIG_BLOCKS"]

        if self.verbosity.value > Verbosity.HIGH.value:
            print("\nGetting " + str(self.sd_card_setup_dict["NUM_CONFIG_BLOCKS"]) + " Config Data Blocks Info {config_block_info_dict}")
        for i in range(self.sd_card_setup_dict["NUM_CONFIG_BLOCKS"]):
            if self.verbosity.value > Verbosity.HIGH.value:
                print("\n    Reading CFG_" + str(i))
            for key, value in yaml.safe_load(open(self.config_file_path))['CFG_' + str(i)].items():
                self.config_block_info_dict["CFG_" + str(i) + ":" + key] = value
                if self.verbosity.value > Verbosity.HIGH.value:
                    print("\t" + "CFG_" + str(i) + ":" + key + "\t" + str(value))

        # get actual data info
        self.num_data_blocks = self.sd_card_setup_dict["NUM_DATA_BLOCKS"]

        if self.verbosity.value > Verbosity.HIGH.value:
            print("\nGetting " + str(self.sd_card_setup_dict["NUM_DATA_BLOCKS"]) + " Data Blocks Info {data_block_info_dict}")
        for i in range(self.sd_card_setup_dict["NUM_DATA_BLOCKS"]):
            if self.verbosity.value > Verbosity.HIGH.value:
                print("\nReading DB_" + str(i))
            for key, value in yaml.safe_load(open(self.config_file_path))['DB_' + str(i)].items():
                self.data_block_info_dict["DB_" + str(i) + ":" + key] = value
                if self.verbosity.value > Verbosity.HIGH.value:
                    print("\t" + "DB_" + str(i) + ":" + key + "\t" + str(value))


        # get config math blocks
        if self.verbosity.value > Verbosity.HIGH.value:
            print("\nGetting" + str(self.sd_card_setup_dict["NUM_CFG_MATH_BLOCKS"]) + " Config Math")
        for i in range(self.sd_card_setup_dict["NUM_CFG_MATH_BLOCKS"]):
            if self.verbosity.value > Verbosity.HIGH.value:
                print("\nReading MATH_CFG_" + str(i))
            for key, value in yaml.safe_load(open(self.config_file_path))['DB_MATH_' + str(i)].items():
                self.

        # get actual data math blocks

        # print out that the yaml database is completely read if verbosity is high enough
        if self.verbosity.value > Verbosity.HIGH.value:
            print("\nYAML file read in completely\n")





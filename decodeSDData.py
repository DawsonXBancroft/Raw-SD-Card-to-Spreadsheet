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
# example use WINDOWS:
# python decodeSDData.py -type DEBUG -inputfile .\ExampleInput\210708_FLIGHT_DATAONLY_LORA_ONLY.txt -verbosity DEBUG
# example use LINUX:
# python decodeSDData.py -type DEBUG -inputfile ExampleInput/210708_FLIGHT_DATAONLY_LORA_ONLY.txt -verbosity DEBUG

import sys
sys.path.append('classes/')
# User defined classes
from yaml_config import *
from yaml_math import *
from verbosity import *
from cmdline_args_parse import *
from csv_writer import *
from raw_reader import *
from transaction import *


def __main__():
    # PARSE COMMAND LINE ARGUMENTS
    cmd_cfg = CMDLineParser()
    cmd_cfg.parse()

    # READ IN YAML (config) FILE
    yaml_cfg = YamlConfig()
    yaml_cfg.config_file_path = cmd_cfg.config_file_path
    yaml_cfg.verbosity = cmd_cfg.verbosity
    yaml_cfg.readInConfig()

    # INITIALIZE YAML MATH
    yaml_math = YamlMath()
    yaml_math.yaml_cfg = yaml_cfg
    yaml_math.verbosity = cmd_cfg.verbosity

    # IF CONFIG DATA READ THAT IN (MAY CONTAIN # OF DATA POINTS)
    if (yaml_cfg.sd_card_setup_dict["DATA_POINTS_IN_CONFIG"] == True):
        num_items = yaml_cfg.math_config_dict["DATAPOINTS"]
        if cmd_cfg.verbosity.value > Verbosity.HIGH.value:
            print("\nValue taken from config file to be on SD Card\n")
    else:
        num_items = cmd_cfg.datapoints
        if cmd_cfg.verbosity.value > Verbosity.HIGH.value:
            print("\nNumber datapoints value taken from command line to be " + str(cmd_cfg.datapoints) + "\n")

    # READ IN DATA AND SEND IT TO THE CSV WRITER

        # CREATE THE READER
    raw_r = RawReader()
    raw_r.verbosity = cmd_cfg.verbosity
    raw_r.input_file_path = cmd_cfg.input_file_path
    raw_r.cfg = yaml_cfg
    raw_r.datapoints = num_items
    raw_r.openFile()

        # CREATE THE CSV WRITER
    csv_w = CSVWriter()
    csv_w.verbosity = cmd_cfg.verbosity
    csv_w.output_file_path = cmd_cfg.output_file_path
    csv_w.openCSVFile()
    csv_w.writeHeaders(list(yaml_cfg.col_labels_dict.values()))

        # SET CSV WRITER TO
    raw_r.writer = csv_w

        # READER START
    # print(len(yaml_cfg.config_block_info_dict)) # debug
    # print(len(yaml_cfg.data_block_info_dict))   # debug

    # create transaction to be used to print data
    this_block = Transaction()

    # keep track of current data block
    block_num = 0

    # read config blocks
    for i in range(yaml_cfg.num_config_blocks):
        this_block = raw_r.readBlock(block_num)

        # do math and add data to a dictionary if necessary

        block_num = block_num + 1


    # read data blocks
    for i in range(cmd_cfg.datapoints):
        for j in range(yaml_cfg.num_data_blocks):
            this_block = raw_r.readBlock(block_num)

            # print(this_block.convert2string())
            yaml_math.add_to_block_array(this_block)
            block_num = block_num + 1
        yaml_math.do_math()

    print()
    # CLOSE ALL OPEN FILES
    raw_r.closeFile()
    csv_w.closeCSVFile()

__main__()

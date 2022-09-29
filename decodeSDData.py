# @author: DawsonXBancroft
# example use WINDOWS:
# python decodeSDData.py -type DEBUG -inputfile .\ExampleInput\210708_FLIGHT_DATAONLY_LORA_ONLY.txt -verbosity DEBUG
# example use LINUX:
# python decodeSDData.py -type DEBUG -inputfile ExampleInput/210708_FLIGHT_DATAONLY_LORA_ONLY.txt -verbosity DEBUG
import sys
sys.path.append('classes/')
# User defined classes
from yaml_config import *
from verbosity import *
from cmdline_args_parse import *
from csv_writer import *


def __main__():
    # PARSE COMMAND LINE ARGUMENTS
    cmd_cfg = CMDLineParser()
    cmd_cfg.parse()

    # READ IN YAML (config) FILE
    yaml_cfg = YamlConfig()
    yaml_cfg.config_file_path = cmd_cfg.config_file_path
    yaml_cfg.verbosity = cmd_cfg.verbosity
    yaml_cfg.readInConfig()

    # IF CONFIG DATA READ THAT IN (MAY CONTAIN # OF DATA POINTS)
    if (yaml_cfg.sd_card_setup_dict["DATA_POINTS_IN_CONFIG"] == True):
        num_items = yaml_cfg.math_config_dict["DATAPOINTS"]
        if cmd_cfg.verbosity.value > Verbosity.HIGH.value:
            print("\nValue taken from config file to be on SD Card\n")
    else:
        num_items = cmd_cfg.datapoints
        if cmd_cfg.verbosity.value > Verbosity.HIGH.value:
            print("\nValue taken from command line to be " + cmd_cfg.datapoints + "\n")

    # READ IN DATA AND SEND IT TO THE CSV WRITER

        # FIRST CREATE THE CSV WRITER
    csv_w = CSVWriter()
    csv_w.verbosity = cmd_cfg.verbosity
    csv_w.output_file_path = cmd_cfg.output_file_path
    csv_w.openCSVFile()
    csv_w.writeHeaders(list(yaml_cfg.col_labels_dict.values()))

    # CLOSE ALL OPEN FILES
    csv_w.closeCSVFile()

__main__()

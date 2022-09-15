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


def __main__():
    # PARSE COMMAND LINE ARGUMENTS
    cmd_cfg = CMDLineParser()
    cmd_cfg.parse()

    # READ IN YAML (config) FILE
    yaml_cfg = YamlConfig(cmd_cfg.config_file_path, cmd_cfg.verbosity)
    yaml_cfg.readInConfig()

    # IF CONFIG DATA READ THAT IN (MAY CONTAIN # OF DATA POINTS)


    # READ IN DATA


__main__()

# @author: DawsonXBancroft
# example use:
# python decodeSDData.py -type DEBUG -inputfile .\ExampleInput\210708_FLIGHT_DATAONLY_LORA_ONLY.txt
import sys
sys.path.append('classes/')
# User defined classes
from yaml_config import *
from verbosity import *
from cmdline_args_parse import *


def __main__():
    # PARSE COMMAND LINE ARGUMENTS
    sd_cfg = CMDLineParser()
    sd_cfg.parse()

    # READ IN YAML (config) FILE
    yaml_cfg = YamlConfig(sd_cfg.config_file_path)
    yaml_cfg.readInConfig()

    # IF CONFIG DATA READ THAT IN (MAY CONTAIN # OF DATA POINTS)


    # READ IN DATA


__main__()

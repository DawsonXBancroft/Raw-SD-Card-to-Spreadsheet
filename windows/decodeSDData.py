# @author: DawsonXBancroft
# example use:
# python decodeSDData.py -type DEBUG -inputfile .\ExampleInput\210708_FLIGHT_DATAONLY_LORA_ONLY.txt
import sys
import os.path
import yaml
from enum import Enum


class Verbosity(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    DEBUG = 4


verbosity = Verbosity.MEDIUM
input_file_path = "null"
config_file_path = "null"
output_file_path = "null"
gui = False
usage = "Usage: main.py [-inputfile <PATH> -type <{DEBUG, NO_ATTACH, NEMO}> [-outputfile <PATH>] [-verbosity <{LOW, " \
        "MEDIUM, HIGH, DEBUG}>]] || [-gui]] "


def parseCommandLineArgs():
    args = sys.argv[1:]
    global verbosity
    global input_file_path
    global config_file_path
    global output_file_path
    global gui
    global usage
    if len(args) == 0:
        print(usage)
        sys.exit()
    for i in range(0, len(args), 1):
        if args[i] == "-verbosity":
            if args[i + 1] == "HIGH":
                verbosity = Verbosity.HIGH
                i = i + 1
            elif args[i + 1] == "MEDIUM":
                verbosity = Verbosity.MEDIUM
                i = i + 1
            elif args[i + 1] == "LOW":
                verbosity = Verbosity.LOW
                i = i + 1
            elif args[i + 1] == "DEBUG":
                verbosity = Verbosity.DEBUG
                i = i + 1
            else:
                print("FATAL: VERBOSITY IS INVALID")
                print("       Please use -verbosity [LOW, MEDIUM, HIGH, DEBUG]")
                sys.exit()
        elif args[i] == "-inputfile":
            if os.path.exists(args[i + 1]):
                input_file_path = args[i + 1]
                i = i + 1
            else:
                print("FATAL: INPUT FILE DOES NOT EXIST")
                print("       Please ensure filepath is correct and the file exists.")
                sys.exit()
        elif args[i] == "-outputfile":
            if os.path.exists(args[i + 1]):
                usr_input = input("File " + args[i + 1] + " exists. Would you like to overwrite it? (y/n)")
                if usr_input.lower() == "y":
                    output_file_path = args[i + 1]
                    i = i + 1
                else:
                    print("Okay; Exiting program")
                    sys.exit()
            else:
                output_file_path = args[i + 1]
                i = i + 1
        elif args[i] == "-type":
            if args[i + 1].upper() == "DEBUG":
                config_file_path = "config/debug.yaml"
                i = i + 1
            else:
                print("FATAL: NO TYPE FOUND FOR " + args[i + 1])  # TODO: REPLACE WITH STD FILE
                sys.exit()
        elif args[i] == "-gui":
            gui = True

    if verbosity.value > Verbosity.HIGH.value:
        print("END OF PARSING ARGUMENTS")
        print("    verbosity     : " + verbosity.name)
        print("    gui           : " + str(gui))
        print("    input file    : " + input_file_path)
        print("    output file   : " + output_file_path)
        print("    type          : " + config_file_path)
        print()

    if not gui:
        if input_file_path == "null":
            print("FATAL: INPUT FILE NOT SPECIFIED")
            print(usage)
            sys.exit()
        if config_file_path == "null":
            print("FATAL: TYPE NOT SPECIFIED")
            print(usage)
            sys.exit()


def configRead():
    global config_file_path

    col_labels_dict = {}
    col_vars_dict = {}
    sd_card_setup_dict = {}
    # get column labels (column headers for csv file)
    for key, value in yaml.safe_load(open(config_file_path))['COL_LABELS'].items():
        print(key, value)

    # get column vars (variables that will go in each row of the csv file)
    for key, value in yaml.safe_load(open(config_file_path))['COL_VARS'].items():
        print(key, value)

    # get sd card setup
    for key, value in yaml.safe_load(open(config_file_path))['SDCARD_SETUP'].items():
        print(key, value)



def __main__():
    # PARSE COMMAND LINE ARGUMENTS
    parseCommandLineArgs()

    # READ IN YAML (config) FILE
    configRead()

    # IF CONFIG DATA READ THAT IN (MAY CONTAIN # OF DATA POINTS)

    # READ IN DATA


__main__()



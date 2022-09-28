import yaml
import sys
from verbosity import *
class YamlConfig():

    # Class for holding configuration of SD Card and CSV file
    config_file_path = "null"
    col_labels_dict = {}
    col_vars_dict = {}
    sd_card_setup_dict = {}
    config_block_info_dict = {}
    data_block_info_dict = {}

    math_config_dict = {}
    math_data_dict = {}


    # When constructed, the config_file_path is required
    def __init__(self, config_file_path, verbosity):
        self.config_file_path = config_file_path
        self.verbosity = verbosity

    def readInConfig(self):
        # get column labels (column headers for csv file)
        if self.verbosity.value > Verbosity.HIGH.value:
            print("\nGetting Column Labels")
        for key, value in yaml.safe_load(open(self.config_file_path))['COL_LABELS'].items():
            self.col_labels_dict[key] = value
            if self.verbosity.value > Verbosity.HIGH.value:
                print("\t" + str(key) + "\t" + str(value))



        # get column vars (variables that will go in each row of the csv file)
        if self.verbosity.value > Verbosity.HIGH.value:
            print("\nGetting Column Variables")
        for key, value in yaml.safe_load(open(self.config_file_path))['COL_VARS'].items():
            self.col_vars_dict[key] = value
            if self.verbosity.value > Verbosity.HIGH.value:
                print("\t" + str(key) + "\t" + str(value))

        # get sd card setup
        if self.verbosity.value > Verbosity.HIGH.value:
            print("\nGetting Column SD Card Setup")
        for key, value in yaml.safe_load(open(self.config_file_path))['SDCARD_SETUP'].items():
            self.sd_card_setup_dict[key] = value
            if self.verbosity.value > Verbosity.HIGH.value:
                print("\t" + str(key) + "\t" + str(value))

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
        if self.verbosity.value > Verbosity.HIGH.value:
            print("\nGetting " + str(self.sd_card_setup_dict["NUM_CONFIG_BLOCKS"]) + " Config Data Blocks Info")
        for i in range(self.sd_card_setup_dict["NUM_CONFIG_BLOCKS"]):
            if self.verbosity.value > Verbosity.HIGH.value:
                print("\n    Reading CFG_" + str(i))
            for key, value in yaml.safe_load(open(self.config_file_path))['CFG_' + str(i)].items():
                self.config_block_info_dict["CFG_" + str(i) + ":" + key] = value
                if self.verbosity.value > Verbosity.HIGH.value:
                    print("\t" + str(key) + "\t" + str(value))

        # get actual data info
        if self.verbosity.value > Verbosity.HIGH.value:
            print("\nGetting " + str(self.sd_card_setup_dict["NUM_DATA_BLOCKS"]) + " Data Blocks Info")
        for i in range(self.sd_card_setup_dict["NUM_DATA_BLOCKS"]):
            if self.verbosity.value > Verbosity.HIGH.value:
                print("\nReading DB_" + str(i))
            for key, value in yaml.safe_load(open(self.config_file_path))['DB_' + str(i)].items():
                self.data_block_info_dict["DB_" + str(i) + ":" + key] = value
                if self.verbosity.value > Verbosity.HIGH.value:
                    print("\t" + str(key) + "\t" + str(value))


        # print out that the yaml database is completely read if verbosity is high enough
        if self.verbosity.value > Verbosity.HIGH.value:
            print("\nYAML file read in completely\n")







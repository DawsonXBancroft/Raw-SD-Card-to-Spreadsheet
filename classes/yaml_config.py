import yaml
class YamlConfig():

    # Class for holding configuration of SD Card and CSV file
    config_file_path = "null"
    col_labels_dict = {}
    col_vars_dict = {}
    sd_card_setup_dict = {}


    # When constructed, the config_file_path is required
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path

    def readInConfig(self):
        # get column labels (column headers for csv file)
        for key, value in yaml.safe_load(open(self.config_file_path))['COL_LABELS'].items():
            print(key, value)

        # get column vars (variables that will go in each row of the csv file)
        for key, value in yaml.safe_load(open(self.config_file_path))['COL_VARS'].items():
            print(key, value)

        # get sd card setup
        for key, value in yaml.safe_load(open(self.config_file_path))['SDCARD_SETUP'].items():
            print(key, value)


# @author: DawsonXBancroft
import string
import sys

def parseCommandLineArgs():
    args = sys.argv[1:]
    for i in range(0, len(args), 1):
        if args[i] == "-verbosity":
            if (args[i+1] == "HIGH") or (args[i+1] == "MEDIUM") or (args[i+1] == "LOW") or (args[i+1] == "DEBUG"):
                


def main():
    VERBOSITY = "MEDIUM"
    # PARSE COMMAND LINE ARGUMENTS

    # SET INPUT FILE, OUTPUT FILE, AND CONFIG INPUT FILE

    # READ IN YAML FILE

    # IF CONFIG DATA READ THAT IN (MAY CONTAIN # OF DATA POINTS)

    # READ IN DATA


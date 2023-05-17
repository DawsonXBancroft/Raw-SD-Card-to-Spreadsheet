# SDCardRawReader
Python is used to convert the raw files spreadsheets. Mainly used get bakPack or LoRad data off of microSD cards.

# Steps
First you need to get the data off of the SD card into a .raw file. Next, convert that data from raw data to a text file. Then convert the text file information into a spreadsheet.

1. **WARNING:** `dd` **is a super strong command. Overview the man pages for** `dd` **before using it. You will need to TRIPLE check as otherwise you might overwrite your harddrive.** Use the `dd` command to copy the data over from the SD card to a file. i.e.: `dd if=/dev/mmcblk0 of=/home/[username]/Desktop/sdcard_[date].raw`

2. Use `hexdump` to convert the raw file into readable data for python. i.e.: `hexdump -v -C /home/[username]/Desktop/sdcard_[date].raw > /home/[username]/Desktop/sdcard_[date].txt`

3. Use the python program to take in the txt file and output a formatted and calculated csv file.

# decodeSDData.py
This is the Python program to convert the data input from text file (and possibly directly from the SD card in the future) to an Excel workbook (.csv file).

Usage: ```decodeSDData.py [-inputfile <PATH> -type <{DEBUG, NO_ATTACH, NEMO}> [-outputfile <PATH>] [-verbosity [<LOW, MEDIUM, HIGH, DEBUG}>]] || [-gui]] ```

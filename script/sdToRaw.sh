if [ $# -eq 0 ]
then
	echo "No input arguments. So what path and file would you like to create?"
	read OUTPUT_FILE
else
	OUTPUT_FILE=$1
fi

cd ..

TEMP_FILE="temp.raw"

echo "COPYING FILES FROM SD CARD"

sudo dd if=/dev/mmcblk0 of="$TEMP_FILE" >& /dev/null

echo "DATA FROM SD CARD COPIED -- CREATING TEXT FILE NOW"
echo "Feel free to remove or erase the SD card now"

hexdump -C "$TEMP_FILE" > "$OUTPUT_FILE"

echo "OPERATIONS COMPLETE -- CLEANING UP NOW"

rm -f "temp.ra"

cd script

echo "fin"

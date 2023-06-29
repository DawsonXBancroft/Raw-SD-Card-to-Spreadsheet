#!/usr/bin/zsh

for (( i=0; i<=511; i++ ))
do
	#echo "COL_"$i"\t\t: \"BYTE_"$i"_OUT\""
	#echo "COL_"$i"\t\t: \"BYTE_"$i"\""
	echo "BYTE_"$i"_OUT:\t\t\"=,BYTE_"$i"_IN\""
done

debug:
	python decodeSDData.py -type DEBUG -inputfile ExampleInput/test_hexfile.txt -verbosity DEBUG -datapoints 2

simple:
	python decodeSDData.py -type SIMPLE -inputfile ExampleInput/test_hexfile.txt -verbosity DEBUG -datapoints 2

clean:
	rm -rf OutputFiles/*

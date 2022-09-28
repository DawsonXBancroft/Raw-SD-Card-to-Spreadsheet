debug:
	python decodeSDData.py -type DEBUG -inputfile ExampleInput/210708_FLIGHT_DATAONLY_LORA_ONLY.txt -verbosity DEBUG -datapoints 20

clean:
	rm -rf OutputFiles/*

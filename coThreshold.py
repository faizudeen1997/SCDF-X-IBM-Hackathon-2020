#Retrieve the 10 most recent voltage values of MQ-7 from the MQDB
data = []

# Using CO threshold of 55ppm from MQ-7
# Since MQ-7 range is 10ppm to 500ppm, required voltage threshold is ~0.45V
# Return True if average Voltage of dataSet values >= 0.45V
def coThreshold(dataSet):
	return sum(dataSet)//len(dataSet) >= 0.45

print(coThreshold(data))
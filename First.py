#Program to populate data in pipeline text file and SensorError text file
# This program addresses Problem 1 and 2
import random as rand
import datetime

sensor = []
error = []
pipeline = []
j = 0
i = 0
k = 0
num =16

# Data genereated with Error message
while i != 31:
    while j != 16:
        dataset = format(rand.random(), '.2f')
        sensor.append(dataset)
        j +=1
    if len(sensor) == num:
        pipeline.append(sensor)
    i +=1
# Adds Error string "err" in data set
if i == 31:
    for k in range(16):
        error.append('err')
    if len(error) == num:
        pipeline.append(error)
else:
    print(i)

pipelinestring = list(enumerate(pipeline))
#print(pipelinestring)

# Creates pipeline text file
file = open("pipelinefile.txt", "a")
file.write("\n")
file.write (datetime.datetime.now().ctime())
file.write("\n")
file.write('\n'.join('%s %s' % x for x in pipelinestring))

file.close()



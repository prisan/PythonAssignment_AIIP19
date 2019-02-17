# Program to check for Error string in data
# The program addresses problem 3
import datetime

sensor = []
error = []
pipeline = []
j = 0
i = 0
k = 0
num =16

# Creates Error text file
ErrorFile = open("SensorError.txt",'a')
ErrorFile.write("\n")
ErrorFile.write(datetime.datetime.now().ctime())
ErrorFile.write("\n")

# Error Check Function
def ErrorCheck():
    with open("pipelinefile.txt","r") as openfile:
        for line in openfile:
            for part in line.split():
                # Checks for error string
                if 'err' in part:
                    ErrorFile = open("SensorError.txt", 'a')
                    #ErrorFile.write(line) # This line is being replced in the error log with a numerical value
                    ErrorFile.write(part.replace('err', '21'))

#Calling the Error
ErrorCheck()


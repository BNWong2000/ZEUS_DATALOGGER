'''
Created on Oct. 30, 2020

@author: Sam
'''
import csv
import time


# Fake Data
batteryTemp = [24, 23, 45, 56, 34, 65, 78, 69]
coolingLoopTemp = [27, 24, 49, 53, 33, 68, 71, 62]
batteryVoltage = [3, 4, 5, 6, 7, 8, 9, 2]
batteryCurrent = [1, 2, 3, 4, 5, 6, 7, 8]
speedData = [11, 12, 13, 14, 15, 16, 17, 18]
locationData = [[1, 2], [2, 1], [2, 2], [2, 2], [3, 2], [2, 3], [4, 2], [2, 4]]

# Opens and Creates Headers
def create_and_format(name):
    with open(name,'w', newline='') as f:
        logger = csv.writer(f)
        logger.writerow(['BatteryTemp', 'CoolingLoopTemp', 'BatteryVoltage', 'BatteryCurrent', 'SpeedData', 'LocationXData','LocationYData'])
       
#takes name and position of the data arrays and writes their values to a new line
def log(name,position):
    with open(name,'a', newline='') as f:
        logger = csv.writer(f)
        logger.writerow([batteryTemp[position], coolingLoopTemp[position], batteryVoltage[position], batteryCurrent[position], speedData[position], locationData[position][0],locationData[position][1]])

def main():
    file_name = "TestInput.csv"
    create_and_format(file_name)
    seconds = 8 #How long to keep writing
    sleep_time = 1 #how long to wait before writing again
    for x in range(0,seconds):#writes data onto the file for a given amount of seconds
        log(file_name,x)
        time.sleep(sleep_time)#delays the write by sleep_time*seconds
main() 
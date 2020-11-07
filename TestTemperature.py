'''
Created on Oct. 30, 2020

@author: Sam
'''
import csv
import time
from datetime import datetime
import Adafruit_DHT
#import pandas

# Fake Data


# Opens and Creates Headers
def create_and_format(name):
    with open(name,'w', newline='') as f:
        logger = csv.writer(f)
        logger.writerow(['Temperature', 'Humidity','Date/Time'])
       
#takes name and position of the data arrays and writes their values to a new line
def log(name):
    with open(name,'a', newline='') as f:
        logger = csv.writer(f) #next 2 lines collects data
        humidity, temperature = Adafruit_DHT.read_retry(11, 4)
        
        now = datetime.now()#Next 2 lines collect Time
        currentTime= now.strftime("%H:%M:%S")
        
        print(temperature, humidity, currentTime)#Prints to console
        
        logger.writerow([temperature, humidity, currentTime])#Writes into csv

def print_average(name):
    with open(name) as csv_file: #opens the csv file
        reader = csv.reader(csv_file, delimiter = ',')#reads the file and says a comma separates the values
        next(reader)#skips past the headers
        totaltemp = 0
        totalhumid = 0
        measurements = 0

        for row in reader:
            temperature, humidity, time = row #Sets values for the current row into their respective variables
            
            totaltemp = totaltemp + float(temperature) # adds all of temp and time
            totalhumid = totalhumid + float(humidity)
            measurements += 1
            
        avetemp = totaltemp / measurements
        avehumidity = totalhumid / measurements
        print(avetemp, avehumidity)

def main():
    file_name = "TestTemp.csv"
    create_and_format(file_name)
    seconds = 10 #How long to keep writing
    sleep_time = 0 #how long to wait before writing again
    for x in range(0,seconds):#writes data onto the file for a given amount of seconds
        log(file_name)
        print_average(file_name)
        time.sleep(sleep_time)#delays the write by sleep_time*seconds
        
main()
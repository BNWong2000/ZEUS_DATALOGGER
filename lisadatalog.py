import csv
import time

# Fake Data
batteryTemp = [24, 23, 45, 56, 34, 65, 78, 69]
coolingLoopTemp = [27, 24, 49, 53, 33, 68, 71, 62]
batteryVoltage = [3, 4, 5, 6, 7, 8, 9, 2]
batteryCurrent = [1, 2, 3, 4, 5, 6, 7, 8]
speedData = [11, 12, 13, 14, 15, 16, 17, 18]
locationData = [[1, 2], [2, 1], [2, 2], [2, 2], [3, 2], [2, 3], [4, 2], [2, 4]]


def create_file(filename):
    with open(filename, 'w', newline='') as f:
        datafile = csv.writer(f)
        datafile.writerow(["batteryTemp" , "coolingLoopTemp" , "batteryVoltage" , "batteryCurrent" ,
                           "speedData" ,  "locationXData" , "locationYData"])
    return datafile


def write_data(file, data):
    f = open(file, 'a')
    datafile = csv.writer(f)
    datafile.writerow(data)
    return datafile


def get_data(index):
    data = [str(batteryTemp[index]), str(coolingLoopTemp[index]), str(
        batteryVoltage[index]), str(batteryCurrent[index]), str(speedData[index]), str(
        locationData[index][0]), str(locationData[index][1])]
    return data


def main():
    filename = 'bike_data.csv'
    create_file(filename)
    time_elapsed = 0
    time_delay = 1

    while time_elapsed < 8:
        sensor_data = get_data(time_elapsed)
        write_data(filename, sensor_data)
        time.sleep(time_delay)
        print("Delay by " + str(time_delay) + " seconds")
        print(*sensor_data, sep=',')
        time_elapsed += 1


main()






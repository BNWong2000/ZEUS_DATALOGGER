import csv
import time

# Fake Data
batteryTemp = [24, 23, 45, 56, 34, 65, 78, 69]
coolingLoopTemp = [27, 24, 49, 53, 33, 68, 71, 62]
batteryVoltage = [3, 4, 5, 6, 7, 8, 9, 2]
batteryCurrent = [1, 2, 3, 4, 5, 6, 7, 8]
speedData = [11, 12, 13, 14, 15, 16, 17, 18]
locationData = [[1, 2], [2, 1], [2, 2], [2, 2], [3, 2], [2, 3], [4, 2], [2, 4]]


def createCSV(fileName):
    fileName = "C:/Users/sjamal/IdeaProjects/DataLogger/" + fileName
    file = open(fileName, 'w', newline='')

    return file


def getSensorData(timeIndex):
    data = str(batteryTemp[timeIndex]) + "," + str(coolingLoopTemp[timeIndex]) + "," + str(
        batteryVoltage[timeIndex]) + "," + str(batteryCurrent[timeIndex]) + "," + str(speedData[timeIndex]) + "," + str(
        locationData[timeIndex][0]) + "," + str(locationData[timeIndex][1])
    # print(data)
    return data


def writeToCSV(file, sensorData):
    file.write(sensorData)
    file.write("\n")


def closeCSV(file):
    file.close()


def main():
    # Create CSV file with name
    csvFileName = "sensor_data_log.csv"
    csvFile = createCSV(csvFileName)

    # Add sensor data column headers
    columnHeaders = "batteryTemp" + "," + "coolingLoopTemp" + "," + "batteryVoltage" + "," + "batteryCurrent" +\
                    "," + "speedData" + "," + "locationXData" + "," + "locationYData"
    writeToCSV(csvFile, columnHeaders)  # Write to CSV file

    # Get sensor Data every second & write to CSV file
    timer = 0
    keepLooping = True
    startTime = time.time()
    while keepLooping == True:
        sensorData = getSensorData(timer)  # Get sensor data
        print(sensorData)

        print(time.time() - startTime)
        print((time.time() - startTime) % 1.0)
        print(1.0 - ((time.time() - startTime) % 1.0))
        print()
        time.sleep(1.0 - ((time.time() - startTime) % 1.0))  # Ensures 1-second between data acquiring

        writeToCSV(csvFile, sensorData)  # Write to CSV file

        timer += 1
        if timer == 8:
            keepLooping = False

    # Close CSV file
    closeCSV(csvFile)

    # Github Demo 1
    # Github Demo 2
    # Github Demo 3
    # Github Demo 4

    # Github Demo Safwan

main()

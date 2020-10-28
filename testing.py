from array import *

i = 0

controllerTemp = [111, 222, 333] # just basic fake data
loopTemp = [1, 2, 3]
batteryTemp = [11, 22, 33]

batteryVoltage = [1111, 2222, 3333] # Battery data format subject to change...
batteryCurrent = [11111, 22222, 33333]

locationData = [[1, 2],[2, 3],[3, 4]] # Location/GPS data

params = 8

def createFile(fileName):
    fileNameCSV = fileName + ".csv"
    f = open(fileNameCSV, "w") # creates the file with the requested file name. 
    return f
    # do something

def writeToFile(file, dataToWrite):
    file.write(dataToWrite)
    file.write("\n")

def closeFile(file):
    file.close()

def getSystemDate():
    return " today" # we would get the actual date from the raspberry pi. this is a placeholder. 


def getData(): # This is a pretty terrible way of doing it, so we'll have to see how the data actually enters the pi.
    samplesIndex = 2 #temp for testing...

    global i
    result = ""
    result += str(controllerTemp[i]) + ","
    result += str(loopTemp[i]) + ","
    result += str(batteryTemp[i]) + ","
    result += str(batteryVoltage[i]) + ","
    result += str(batteryCurrent[i]) + ","
    result += str(locationData[i][0]) + ","
    result += str(locationData[i][1])
    print(result)
    i += 1
    # samples += 1
    return result

def main():
    name = "Data Logging" + getSystemDate()
    dataFile = createFile(name)
    keepLooping = True
    timer = 0
    while keepLooping == True:
        timer += 1 # increment the timer

        # read data from the sensors...

        commaSeparatedData = getData()
        print(commaSeparatedData)
        writeToFile(dataFile, commaSeparatedData)

        if timer == 3:
            closeFile(dataFile)
            keepLooping = False
        # do something
    #end


if __name__ == "__main__":
    main()
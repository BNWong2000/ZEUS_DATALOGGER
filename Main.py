import time
import string

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO")


counter = 0

def printStuff():
    print("hehehe")

def initializePins():
    GPIO.setmode(GPIO.BOARD) #Sets the pin numbering scheme. don't change this.
    print("pins initialized")

def logTime():
    time.sleep(1) 
    global counter
    counter = counter + 1
    writeCounterToFile()
    
def writeCounterToFile():
    global counter
    print(counter)
    myFile = open("logging.txt", "a")
    myFile.write("Time: " + str(counter) + "s\n" )
    myFile.close();

def main():
    initializePins()
    printStuff()
    myFile = open("logging.txt", "w")
    myFile.close() 
    while True:
	logTime()
    print("Ending Program")

    
if __name__ == "__main__":
    main()

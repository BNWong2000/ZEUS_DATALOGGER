import time

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO")

outputInit = False;
inputInit = False;

def printStuff():
    print("hehehe")

def setupInputs():
    inputList = [1, 2] #All the channels for input. 
    GPIO.setup(inputList, GPIO.IN)
    inputInit = True

def setupOutputs():
    outputList = [3, 4] #All the channels for output.
    GPIO.setup(outputList, GPIO.OUT)
    outputInit = True
    

def initializePins():
    GPIO.setmode(GPIO.BOARD) #Sets the pin numbering scheme. don't change this.
    setupInputs()
    setupOutputs()
    
def main():
    initializePins()
    
    printStuff()

    
if __name__ == "__main__":
    main()

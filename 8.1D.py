import smbus                                // it is used to communicate with the i2c devices and it is part of i2c interface
import time                                 // it hepls us to get the cuurent time in millis, seconds, minutes, hours
from colorama import Fore                   // it is used to import the diiferent foreground colors which is given to the text

DEVICE = 0x23                               // this is the default address of the i2c device

ONE_TIME_HIGH_RES_MODE_1 = 0x20             // the is used to get the lenght of input in bytes

bus = smbus.SMBus(1)                        // created an instance of the bus and used to communicate with the i2c device

def convertToNumber(data):                  // creating a function to convert the bytes into integer
  result=(data[1] + (256 * data[0])) / 1.2
  return (result)

def readLight(addr=DEVICE):                 // creating this function to get the input from the device 
  data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE_1)               // this statement takes the data from the default device and get the specfic length of that data
  return convertToNumber(data)                          // returning the numeric data

try:                                            
  while True:                                    // creating an infinte loop which iterates till we get any exception
    lightvalue = int(readLight())                // getting the input from the device
    print(Fore.BLACK + "Light value: " + str(lightvalue) + " lx" + "  --> ", end = " ")         // printing the data obtained from i2c device
    if(lightvalue < 10):                             // if the value of light sensor is less than 10 then this will be printed
        print(Fore.RED + "Too dark outside")
    elif(lightvalue < 30 and lightvalue >= 10):      // if the value of light sensor is less than 30 and greater than 10 then this will be printed
        print(Fore.YELLOW + "Dark outside")
    elif(lightvalue < 200 and lightvalue >= 30):      // if the value of light sensor is less than 200 and greater than 30 then this will be printed
        print(Fore.MAGENTA + "normal light outside")
    elif(lightvalue < 800 and lightvalue >= 200):      // if the value of light sensor is less than 800 and greater than 200 then this will be printed
        print(Fore.GREEN + "Bright outside")
    elif(lightvalue >= 800):           // if the value of light sensor is greater than 800 then this will be printed
        print(Fore.CYAN + "Too bright outside")
    else:                                         // if the range of the data is out of these values than this will be printed
        print(Fore.RED + "The value is not valid")

    time.sleep(1)                               // a delay of one second

except keyboardInterrupt:                     // if any exception occurs than this will iterate
    GPIO.cleanup()                 // it will clean up all the port that we have used 

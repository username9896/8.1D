import smbus
import time
from colorama import Fore

DEVICE = 0x23

ONE_TIME_HIGH_RES_MODE_1 = 0x20

bus = smbus.SMBus(1)

def convertToNumber(data):
  result=(data[1] + (256 * data[0])) / 1.2
  return (result)

def readLight(addr=DEVICE):
  data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE_1)
  return convertToNumber(data)

try:
  while True:
    lightvalue = int(readLight())
    print(Fore.BLACK + "Light value: " + str(lightvalue) + " lx" + "  --> ", end = " ")
    if(lightvalue < 10):
        print(Fore.RED + "Too dark outside")
    elif(lightvalue < 30 and lightvalue >= 10):
        print(Fore.YELLOW + "Dark outside")
    elif(lightvalue < 200 and lightvalue >= 30):
        print(Fore.MAGENTA + "normal light outside")
    elif(lightvalue < 800 and lightvalue >= 200):
        print(Fore.GREEN + "Bright outside")
    elif(lightvalue >= 800):
        print(Fore.CYAN + "Too bright outside")
    else:
        print(Fore.RED + "The value is not valid")

    time.sleep(1)

except keyboardInterrupt:
    GPIO.cleanup()

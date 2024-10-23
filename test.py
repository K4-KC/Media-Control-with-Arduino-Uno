# Importing Libraries 
import serial
import time

arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1)

def write_read(x): 
    arduino.write(bytes(x, 'utf-16'))
    # time.sleep(0.05)
    data = arduino.readline()
    return data

while True:
    num = input("Enter a number: ") # Taking input from user
    if num == 'q':
        break
    value = write_read(num)
    print(value) # printing the value
    print(type(value)) # printing the type of value1
    # print the size of value\
    print(len(value))

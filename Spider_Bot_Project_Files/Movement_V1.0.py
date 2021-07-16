'''
    Author:                                     Jan Veintidos
    Last Modification Date:                     5/22/2021
    Description:                                This code will be written for the initial movement for the spider bot



                            FRONT LEFT                                      FRONT RIGHT
                            (0,3)                                           (4,7)
                                        ==================================
                                        =                                =
                                        =                                =
                                        =                                =
                                        =                                =
                                        =                                =
                                        =                                =
                                        =                                =
                                        =                                =
                                        =                                =
                                        =                                =
                                        =                                =
                                        =                                =
                                        =                                =
                                        ==================================
                            BACK LEFT                                       BACK RIGHT        
                            (8,11)                                          (12,15)
        

'''


#import statements every thing in this file has been installed and configured for global use on the PI
from __future__ import division
import time
import RPi.GPIO as GPIO
import Adafruit_PCA9685

#this will get what you need as far as addresses to use the pulse width modulation 
pwm = Adafruit_PCA9685.PCA9685()

#Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

#function that will handle the start up messeage when the bot begins to move
def startUpMessage():
    print("==================================================================================================================")
    print("Spider Bot Movement Code Starting....")
    print("==================================================================================================================")
    print("\n")


#function that handles back leg position
def leftBackPosition(flag):
    #position is home position
    if(flag == 0):
        pwm.set_pwm(0,0,500)
        pwm.set_pwm(4,0,100)
        pwm.set_pwm(8,0,600)
        pwm.set_pwm(12,0,100)

    #move leg foward from home position
    elif(flag == 1):
        pwm.set_pwm(0,0,100)
        pwm.set_pwm(4,0,500)
        pwm.set_pwm(8,0,200)
        pwm.set_pwm(12,0,600)
    #move leg backwards from home position
    elif(flag == 2):
        pwm.set_pwm(0,0,300)

#function that brings all legs to home position 
def standardHomePosition():
    pwm.set_pwm(0,0,260)
    pwm.set_pwm(4,0,275)
    pwm.set_pwm(8,0,350)
    pwm.set_pwm(12,0,420)


def main():
    #function to call code to print message
    #startUpMessage()

   
    for i in range(5):
        leftBackPosition(0)
        time.sleep(.5)
        leftBackPosition(1)
        
        
    standardHomePosition()
    
main()
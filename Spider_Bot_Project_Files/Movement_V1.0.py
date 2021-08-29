'''
    Author:                                     Jan Veintidos
    Last Modification Date:                     8/28/2021
    Description:                                This code will be written for the initial movement for the spider bot
    Notes:                                      The bot was 3D printed all stl files will be located in a seprate folder in the files if you want to se what the robot 
                                                looks like. Dev__I think this code can be changed to be ran with loops struggling with the initial movement code... 


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


#this function is to test the min and max range of the servos for each leg. 
#can also be used for making sure that all servos are connected correctly and are working properly.
def testingPosition(flag):
    #position is home position
    if(flag == 0):
        #===============================================================
        #front left leg
        #===============================================================
        pwm.set_pwm(0,0,600)
        #pwm.set_pwm(1,0,500)
        #pwm.set_pwm(2,0,100) 
        #===============================================================

        #===============================================================
        #front right leg      
        #===============================================================  
        #pwm.set_pwm(4,0,100)
        #pwm.set_pwm(5,0,100)
        #pwm.set_pwm(6,0,450)
        #===============================================================

        #===============================================================
        #back left leg
        #===============================================================
        #pwm.set_pwm(8,0,600)
        #pwm.set_pwm(9,0,200)
        #pwm.set_pwm(10,0,300)
        #===============================================================

        #===============================================================
        #back right leg
        #===============================================================
        #pwm.set_pwm(12,0,180)
        #pwm.set_pwm(13,0,500)
        #pwm.set_pwm(14,0,400)
        #===============================================================

    #move leg foward from home position
    elif(flag == 1):
        #===============================================================
        #front left leg
        #===============================================================
        pwm.set_pwm(0,0,325)
        #pwm.set_pwm(1,0,140)
        #pwm.set_pwm(2,0,400)
        #===============================================================
        
        #===============================================================
        #front right leg
        #===============================================================
        #pwm.set_pwm(4,0,480)
        #pwm.set_pwm(5,0,450)
        #pwm.set_pwm(6,0,200)
        #===============================================================
        
        #===============================================================
        #back left leg
        #===============================================================
        #pwm.set_pwm(8,0,200)
        #pwm.set_pwm(9,0,600)
        #pwm.set_pwm(10,0,550)

        #===============================================================
        #back right leg
        #===============================================================
        #pwm.set_pwm(12,0,600)
        #pwm.set_pwm(13,0,100)
        #pwm.set_pwm(14,0,130)
        #===============================================================

#function that brings all legs to home position 
def standardHomePosition():
    #home position for main joints 
    pwm.set_pwm(0,0,500)
    pwm.set_pwm(4,0,275)
    pwm.set_pwm(8,0,350)
    pwm.set_pwm(12,0,550)

    #home position for secondary joints
    pwm.set_pwm(1,0,400)
    pwm.set_pwm(5,0,230)
    pwm.set_pwm(9,0,450)
    pwm.set_pwm(13,0,200)

    #home position for third set of joints
    pwm.set_pwm(2,0,290)
    pwm.set_pwm(6,0,300)
    pwm.set_pwm(10,0,475)
    pwm.set_pwm(14,0,175)

#function to move individual legs foward
def fowardPosition(flag):
    #joints that move the positioning of the legs are 0,4,8,12
    #left front leg
    if flag == 0:
        pwm.set_pwm(0,0,600)
    #left back leg
    elif flag == 1:
        pwm.set_pwm(8,0,550)
    #right front leg
    elif flag == 2:
        pwm.set_pwm(4,0,200)
    #right back leg
    elif flag == 3:
        pwm.set_pwm(12,0,300)

def backPosition(flag):
    #joints that move the positioning of the legs 0,4,8,12
    #left front leg
    if flag == 0:
        pwm.set_pwm(0,0,200)
    #left back leg
    elif flag == 1:
        pwm.set_pwm(8,0,250)
    #right front leg
    elif flag == 2:
        pwm.set_pwm(4,0,400)
    #right back leg
    elif flag == 3:
        pwm.set_pwm(12,0,450)

def secondaryJoint(flag):
    #joints that move the positioning of the legs 1,5,9,13
    #left front leg
    if flag == 0:
        pwm.set_pwm(1,0,200)
    #left back leg
    elif flag == 1:
        pwm.set_pwm(9,0,250)
    #right front leg
    elif flag == 2:
        pwm.set_pwm(5,0,400)
    #right back leg
    elif flag == 3:
        pwm.set_pwm(13,0,450)


def main():
    #function to call code to print message
    startUpMessage()

    #function that will call the initial positions for each of the joint positions 
    standardHomePosition()
    time.sleep(1)
   
   #walking forward cycle move two legs on opposite sides front and opposite back foward then raise the two legs that are not being used and 
   #move those foward like the previous legs.  Each cycle needs you to go back to the home position
    
    while True:

        fowardPosition(0)
        time.sleep(1)

        fowardPosition(2)
        time.sleep(1)

        fowardPosition(1)
        time.sleep(1)

        fowardPosition(3)
        time.sleep(1)

        standardHomePosition()
        time.sleep(1)
        
main()
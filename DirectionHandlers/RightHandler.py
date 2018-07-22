"""
Created on Jul 21, 2018

@author: ben
"""

from threading import Thread
from gpiozero import PWMOutputDevice
from time import sleep
import board
import busio
import adafruit_vl6180x


class RightHandler(Thread):
    """
    This will handle the arm movement going right.
    
    I rely on the L298 H bridge with a left and right side.
    I attach BCM 19 to in1, BCM 26 to in2 and connect the grounds to pin 39
    
    PWM_FORWARD_LEFT_PIN = 26# IN1 - Forward Drive                                                                                                                
    PWM_REVERSE_LEFT_PIN = 19# IN2 - Reverse Drive
    Power leads on the motors will have to correspond to the direction appropriatly. 
    As this gets figured out, make notes here. 
    
    This class will set up a thread to monitor the VL6180X adafruit distance estimator. 
    It will probably have to wait every few seconds, as well as make commucations and set
    up the interface between this and the TCA9548A. 
    
    Start small and move on. 1 connection 
    """
    
    def GoForward(self):
        self.forwardLeft.value = 1.0
        self.reverseLeft.value = 0.0
    
    def start(self):
        # IN1 - Forward Drive
        self.L298_LEFT_PWM_FORWARD_PIN = 26
        
        #IN2 - Reverse Drive                                                                                              
        self.L298_LEFT_PWM_REVERSE_PIN = 19
        
        self.forwardLeft = PWMOutputDevice(self.L298_LEFT_PWM_FORWARD_PIN, True, 0, 1000)
        self.reverseLeft = PWMOutputDevice(self.L298_LEFT_PWM_REVERSE_PIN, True, 0, 1000)
        
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.sensor = adafruit_vl6180x.VL6180X(self.i2c)
    
    def run(self):
        self.GoForward()
        while True:
            try:
                """range is in mm"""
                rangemm = self.sensor.range
                status = self.sensor.range_status
                """
                range status could be:
                ERROR_NONE - No error
                ERROR_SYSERR_1 - System error 1 (see datasheet)
                ERROR_SYSERR_5 - System error 5 (see datasheet)
                ERROR_ECEFAIL - ECE failure
                ERROR_NOCONVERGE - No convergence
                ERROR_RANGEIGNORE - Outside range ignored
                ERROR_SNR - Too much noise 
                ERROR_RAWUFLOW - Raw value underflow
                ERROR_RAWOFLOW - Raw value overflow
                ERROR_RANGEUFLOW - Range underflow
                ERROR_RANGEOFLOW - Range overflow
                """
                print()
                if status == adafruit_vl6180x.ERROR_NONE and rangemm < 10.0:
                    return 0
                elif status == adafruit_vl6180x.ERROR_NONE and rangemm < 25.0:
                    sleep(5)
                else:
                    sleep(10)
            finally:
                pass
        
        
        
        
"""
Created on Jul 21, 2018

@author: ben
"""

from threading import Thread
from gpiozero import PWMOutputDevice
from time import sleep
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

    def setup(self, multiplex_handler, right_sensor_channel):
        
        # IN1 - Forward Drive
        self.L298_LEFT_PWM_FORWARD_PIN = 26
        
        #IN2 - Reverse Drive                                                                                              
        self.L298_LEFT_PWM_REVERSE_PIN = 19
        
        self.forwardLeft = PWMOutputDevice(self.L298_LEFT_PWM_FORWARD_PIN, True, 0, 1000)
        self.reverseLeft = PWMOutputDevice(self.L298_LEFT_PWM_REVERSE_PIN, True, 0, 1000)
        
        self.i2c = multiplex_handler.getI2C()
        self.sensor = adafruit_vl6180x.VL6180X(self.i2c)
        
        self.multiplex_handler = multiplex_handler
        self.right_sensor_channel = right_sensor_channel
    
    def GoForward(self):
        self.forwardLeft.value = 1.0
        self.reverseLeft.value = 0.0
    
    def StopForward(self):
        self.forwardLeft.value = 0.0
        self.reverseLeft.value = 0.0
    
    
    def run(self):
        self.multiplex_handler.changeChannel(self.right_sensor_channel)
        self.GoForward()
        try:
            while True:
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
                print("status: %s range %s" % (status, rangemm))
                if status == adafruit_vl6180x.ERROR_NONE and rangemm < 25.0:
                    break
                elif status == adafruit_vl6180x.ERROR_NONE and rangemm < 50.0:
                    sleep(5)
                elif status == adafruit_vl6180x.ERROR_NONE:
                    sleep(5) 
                else:
                    print("Status error: %s" % status)
                    sleep(1)
        finally:
            self.StopForward()
        
        
        
        

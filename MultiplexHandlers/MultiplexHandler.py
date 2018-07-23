"""
Created on Jul 22, 2018

@author: ben
"""

import board
import busio
import smbus2

"""
Bus address of the TCA9548A. It will 
default to 0x70. The user will
be able to change it as they see fit.
"""
MULTIPLEX_ADDRESS = 0x70 

"""
The default I2C bus for the RPi. The
user can to change this too. 
"""
RPI_I2C_BUS = 1

"""
The set of bytes that the user has to pass 
to the change method
"""
MULTIPLEX_CHANNEL_0 = 0B00000001
MULTIPLEX_CHANNEL_1 = 0B00000010
MULTIPLEX_CHANNEL_2 = 0B00000100
MULTIPLEX_CHANNEL_3 = 0B00001000
MULTIPLEX_CHANNEL_4 = 0B00010000
MULTIPLEX_CHANNEL_5 = 0B00100000
MULTIPLEX_CHANNEL_6 = 0B01000000
MULTIPLEX_CHANNEL_7 = 0B10000000

class MultiplexHandler(object):
    """
    This handles the interactions with the Adafruit TCA9548A
    """

    def __init__(self, multiplex_address=0x70, rpi_ic2_bus=1):
        """
        @param multiplex_address: The defined address of the TCA9548A
        @param rpi_ic2_bus: The Raspbery Pi I2C bus to use
        """
        self.MULTIPLEX_ADDRESS = multiplex_address
        self.RPI_I2C_BUS = rpi_ic2_bus
        
        self.bus = smbus2.SMBus(self.RPI_I2C_BUS)
        self.i2c = busio.I2C(board.SCL, board.SDA)
    
    def getI2C(self):
        return self.i2c
    
    def changeChannel(self, channel):
        """
        Change the channel
        """
        if channel not in [MULTIPLEX_CHANNEL_0, MULTIPLEX_CHANNEL_1,
                           MULTIPLEX_CHANNEL_2, MULTIPLEX_CHANNEL_3,
                           MULTIPLEX_CHANNEL_4, MULTIPLEX_CHANNEL_5,
                           MULTIPLEX_CHANNEL_6, MULTIPLEX_CHANNEL_7]:
            return None
        self.bus.write_byte(self.MULTIPLEX_ADDRESS, channel)
        
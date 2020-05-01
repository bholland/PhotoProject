from gpiozero import DigitalOutputDevice
import time
class StepDrive():
    """This will be the class that manages step drives
    """

    def __init__(self):
        self.ENABLE_BCM_PIN = 17
        self.MS1_BCM_PIN = 16
        self.MS2_BCM_PIN = 13
        self.MS3_BCM_PIN = 12
        self.RST_BCM_PIN = 6
        
        self.SLEEP_BCM_PIN = 18
        #self.VCC_BCM_PIN = None # Disconnect this to use the power supply
        self.GND_BCM_PIN = None # This physically attaches to GND
        self.STEP_BCM_PIN = 20
        self.DIRECTION_BCM_PIN = 19

        self.enable = DigitalOutputDevice(self.ENABLE_BCM_PIN)
        self.ms1 = DigitalOutputDevice(self.MS1_BCM_PIN)
        self.ms2 = DigitalOutputDevice(self.MS2_BCM_PIN)
        self.ms3 = DigitalOutputDevice(self.MS3_BCM_PIN)
        self.rst = DigitalOutputDevice(self.RST_BCM_PIN)
        self.sleep_pin = DigitalOutputDevice(self.SLEEP_BCM_PIN)
        #self.vcc = DigitalOutputDevice(self.VCC_BCM_PIN)
        self.step = DigitalOutputDevice(self.STEP_BCM_PIN)
        self.direction = DigitalOutputDevice(self.DIRECTION_BCM_PIN)

        self.enable.off()
        self.rst.on()

        self.sleep_pin.off()
        time.sleep(1)
        self.sleep_pin.on()

        time.sleep(1)
        #self.vcc.on()
        self.direction.on()

        self.ms1.off()
        self.ms2.off()
        self.ms3.off()
        self.step.off()
        
    def setFullStep(self):
        self.ms1.off()
        self.ms2.off()
        self.ms3.off()
        
    def doStep(self):
        self.step.off()
        time.sleep(.01)
        self.step.on()
        time.sleep(.01)
        




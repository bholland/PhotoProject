"""
Created on Jul 21, 2018

@author: ben
"""
import sys
sys.path.append("/home/pi/workspace/PhotoProject/")
print(sys.path)

from DirectionHandlers.RightHandler import RightHandler
from MultiplexHandlers.MultiplexHandler import *
from StepDrive.StepDrive import StepDrive

def main_right():
    """
    main class
    
    start going right
    finally:
        reset
    going right is in its own thread class
    main waits until finished. 
    Perhaps loop on camera photo acceptance or something along those lines.
    Actually, start the photo class and have it manage the camera. 
    """
    multiplex_handler = MultiplexHandler()
    
    right_handler = RightHandler()
    right_handler.setup(multiplex_handler, MULTIPLEX_CHANNEL_0)
    right_handler.start()
    right_handler.join()

def main():
    step_drive = StepDrive()
    step_drive.doStep()

if __name__ == "__main__":
    main()

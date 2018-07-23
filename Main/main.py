"""
Created on Jul 21, 2018

@author: ben
"""
from DirectionHandlers.RightHandler import RightHandler
from MultiplexHandlers.MultiplexHandler import *

def main():
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
    
    right_handler = RightHandler(multiplex_handler, MULTIPLEX_CHANNEL_0)
    right_handler.start()
    right_handler.join()

if __name__ == "__main__":
    main()